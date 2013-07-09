# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.test import TestCase

import versioning
from .models import Revision


class TestFkModel(models.Model):
    attr_text = models.TextField(blank=True)

    class Meta:
        db_table = 'versioning_testfkmodel'


class TestModel(models.Model):
    attr_text = models.TextField(blank=True)
    attr_bool = models.NullBooleanField(blank=True)
    attr_int = models.IntegerField(blank=True, null=True)
    attr_fk = models.ForeignKey(TestFkModel, blank=True, null=True)
    attr_fk_notnull = models.ForeignKey(TestFkModel, related_name='foreign_key_notnull')

    class Meta:
        db_table = 'versioning_testmodel'

versioning.register(
    TestModel,
    ['attr_text', 'attr_int', 'attr_bool', 'attr_fk', 'attr_fk_notnull']
)


class VersioningForAdminTest(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='admin',
            email="admin@mailinator.com",
            password="adminpwd"
        )
        response = self.client.login(username='admin', password='adminpwd')
        self.assertTrue(response)

    def test_diffs(self):
        obj_fk_1 = TestFkModel.objects.create(
            attr_text="техт",
        )
        obj_fk_2 = TestFkModel.objects.create(
            attr_text="техт",
        )
        obj_1 = TestModel(
            attr_text="строка первая\nстрока вторая\nстрока третья",
            attr_fk=None,
            attr_fk_notnull=obj_fk_1,
            attr_int=1
        )
        obj_1.revision_info = {
            'editor': self.admin,
            'comment': 'comment 1',
        }
        obj_1.save()
        self.assertEqual(Revision.objects.get_for_object(obj_1).count(), 1)

        obj_1.save()
        self.assertEqual(Revision.objects.get_for_object(obj_1).count(), 1)

        obj_2 = TestModel.objects.get(pk=obj_1.pk)
        obj_2.attr_text = "строка первая\nстрока измененная вторая\nстрока третья"
        obj_2.attr_bool = True
        obj_2.attr_fk = obj_fk_1
        obj_2.attr_fk_notnull = obj_fk_1
        obj_2.revision_info = {
            'editor': self.admin,
            'comment': 'comment 1',
        }
        obj_2.save()
        self.assertEqual(Revision.objects.get_for_object(obj_1).count(), 2)

        obj_3 = TestModel.objects.get(pk=obj_1.pk)
        obj_3.attr_text = "строка первая\nстрока измененная снова вторая\nстрока третья"
        obj_3.attr_bool = False
        obj_3.attr_int = 3
        obj_3.attr_fk = obj_fk_2
        obj_3.attr_fk_notnull = obj_fk_2
        obj_3.revision_info = {
            'editor': self.admin,
            'comment': 'comment 1',
        }
        obj_3.save()
        self.assertEqual(Revision.objects.get_for_object(obj_1).count(), 3)

        rev_1 = Revision.objects.get_for_object(obj_1).order_by('pk')[0]
        self.assertEqual(rev_1.revision, 1)

        rev_1.display_diff()
        rev_1.reapply()

        obj_4 = TestModel.objects.get(pk=obj_1.pk)
        self.assertEqual(obj_4.attr_text, obj_1.attr_text)
        self.assertEqual(obj_4.attr_bool, obj_1.attr_bool)
        self.assertEqual(obj_4.attr_fk, obj_1.attr_fk)
        self.assertEqual(obj_4.attr_fk_notnull, obj_1.attr_fk_notnull)
        self.assertEqual(Revision.objects.get_for_object(obj_1).count(), 4)
