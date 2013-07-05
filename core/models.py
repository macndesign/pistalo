# coding: utf-8
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class GaleriaQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class GaleriaManager(models.Manager):
    def get_query_set(self):
        return GaleriaQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()


class Galeria(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Ordenação', default=0)
    nome = models.CharField(max_length=120)
    desc = models.TextField(u'Descrição', blank=True)
    imagem = models.ImageField(upload_to='galeria')
    thumb = ImageSpecField(source='imagem', processors=[ResizeToFill(160, 160)], format='JPEG', options={'quality': 60})
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    objects = GaleriaManager()

    class Meta:
        ordering = ['ordenacao', 'nome']

    def __unicode__(self):
        return self.nome
