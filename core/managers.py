# coding: utf-8
from django.db import models


class AtivoQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class AtivoManager(models.Manager):
    def get_query_set(self):
        return AtivoQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()
