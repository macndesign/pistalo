from __future__ import absolute_import, unicode_literals
import copy
import hashlib
try:
    from django.utils import timezone as datetime
except ImportError:
    from datetime import datetime

from django.db import models, IntegrityError
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from . import _registry
from .managers import RevisionManager
from .utils import dmp, diff_split_by_fields, get_field_data, set_field_data

try:
    str = unicode  # Python 2.* compatible
except NameError:
    pass

UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User') 

class Revision(models.Model):
    """
    A single revision for an object.
    """
    object_id = models.CharField(max_length=255, db_index=True)
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey("content_type", "object_id")

    revision = models.IntegerField(_("Revision Number"), db_index=True)
    reverted = models.BooleanField(_("Reverted Revision"), default=False,
                                   db_index=True)
    sha1 = models.CharField(max_length=40, db_index=True)
    delta = models.TextField()

    created_at = models.DateTimeField(_("Created at"), default=datetime.now,
                                      db_index=True)
    comment = models.CharField(_("Editor comment"), max_length=255,
                               blank=True)

    editor = models.ForeignKey(UserModel, verbose_name=_('Editor'),
                               blank=True, null=True,
                               on_delete=models.SET_NULL)
    editor_ip = models.IPAddressField(_("IP Address of the Editor"),
                                      blank=True, null=True)

    objects = RevisionManager()

    class Meta:
        verbose_name = _('Revision')
        verbose_name_plural = _('Revisions')
        get_latest_by = 'id'
        ordering = ('-id',)
        unique_together = (("object_id", "content_type", "revision"),)

    def __str__(self):
        return "r{0} {1} {2}".format(self.revision, self.sha1,
                                     self.content_object)

    def save(self, *a, **kw):
        """ Saves the article with a new revision.
        """
        self.sha1 = hashlib.sha1(
            force_unicode(self.delta).encode("utf-8")
        ).hexdigest()
        if self.id is None:
            try:
                self.revision = Revision.objects.get_for_object(
                    self.content_object
                ).latest().revision + 1
            except self.DoesNotExist:
                self.revision = 1
        attempt = 0
        while True:
            try:
                super(Revision, self).save(*a, **kw)
                break
            except IntegrityError:
                self.revision += 1
                attempt += 1
                if attempt > 20:
                    raise

    def is_anonymous_change(self):
        """Returns True if editor is not authenticated."""
        return self.editor is None

    def reapply(self, editor_ip=None, editor=None):
        """
        Returns the Content object to this revision.
        """
        # Exclude reverted revisions?
        next_changes = Revision.objects.get_for_object(
            self.content_object
        ).filter(
            revision__gt=self.revision
        ).order_by('-revision')

        content_object = self.content_object

        model = self.content_object.__class__
        fields = _registry[model]
        for changeset in next_changes:
            diffs = diff_split_by_fields(changeset.delta)
            for key, diff in diffs.items():
                model_name, field_name = key.split('.')
                if model_name != model.__name__ or field_name not in fields:
                    continue
                content = get_field_data(content_object, field_name)
                patch = dmp.patch_fromText(diff)
                content = dmp.patch_apply(patch, content)[0]
                
                set_field_data(content_object, field_name, content)
                
            changeset.reverted = True
            changeset.save()

        content_object.revision_info = {
            'comment': "Reverted to revision #{0}".format(self.revision),
            'editor_ip': editor_ip,
            'editor': editor
        }
        content_object.save()
        #self.save()

    def display_diff(self):
        """Returns a HTML representation of the diff."""
        # well, it *will* be the old content
        old = copy.copy(self.content_object)

        # newer non-reverted revisions of this content_object,
        # starting from this
        if not self.delta:
            return ""
        newer_changesets = Revision.objects.get_for_object(
            self.content_object
        ).filter(revision__gte=self.revision)

        model = self.content_object.__class__
        fields = _registry[model]
        # apply all patches to get the content of this revision
        for i, changeset in enumerate(newer_changesets):
            diffs = diff_split_by_fields(changeset.delta)
            if len(newer_changesets) == i + 1:
                # we need to compare with the next revision
                # after the change
                next_rev = copy.copy(old)
            for key, diff in diffs.items():
                model_name, field_name = key.split('.')
                if model_name != model.__name__ or field_name not in fields:
                    continue
                patches = dmp.patch_fromText(diff)
                
                set_field_data(
                    old, 
                    field_name, 
                    dmp.patch_apply(
                        patches,
                        get_field_data(old, field_name)
                    )[0]
                )

        result = []
        for field_name in fields:
            result.append("<b>{0}</b>".format(field_name))
            diffs = dmp.diff_main(
                get_field_data(old, field_name),
                get_field_data(next_rev, field_name)
            )
            dmp.diff_cleanupSemantic(diffs)
            result.append(dmp.diff_prettyHtml(diffs))
        return "<br />\n".join(result)

# Python 2.* compatible
try:
    unicode
except NameError:
    pass
else:
    for cls in (Revision, ):
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda self: self.__unicode__().encode('utf-8')
