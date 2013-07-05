# coding: utf-8
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from .managers import AtivoManager


class Autor(models.Model):
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

    objects = AtivoManager()

    class Meta:
        ordering = ['ordenacao', 'nome']
        verbose_name_plural = u'Autores'

    @models.permalink
    def get_absolute_url(self):
        return 'core:autor', (), {'pk': self.pk}

    def __unicode__(self):
        return self.nome


class Galeria(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Ordenação', default=0)
    nome = models.CharField(max_length=120)
    desc = models.TextField(u'Descrição', blank=True)
    imagem = models.ImageField(upload_to='galeria')
    thumb = ImageSpecField(source='imagem', processors=[ResizeToFill(160, 160)], format='JPEG', options={'quality': 60})
    autor = models.ForeignKey(Autor, null=True, blank=True)
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

    objects = AtivoManager()

    class Meta:
        ordering = ['ordenacao', 'nome']

    def __unicode__(self):
        return self.nome


class Sugestao(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Ordenação', default=0)
    titulo = models.CharField(u'Título', max_length=120)
    desc = models.TextField(u'Descrição', blank=True)
    link = models.URLField(blank=True)
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

    objects = AtivoManager()

    class Meta:
        ordering = ['ordenacao', 'titulo']
        verbose_name = u'Sugestão'
        verbose_name_plural = u'Sugestões'

    def __unicode__(self):
        return self.titulo
