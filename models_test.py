from django.db import models


class Pais(models.Model):
    nombre = models.CharField(unique=False, blank=True, null=True, db_column="nombre", verbose_name="nombre", max_length=20)
    codigo_pais = models.IntegerField(unique=False, blank=True, null=True, db_column="codigo_pais", verbose_name="codigo_pais", max_length=2)
     = models.


class Estado(models.Model):
    nombre = models.CharField(unique=False, blank=True, null=True, db_column="nombre", verbose_name="nombre", max_length=30)
    codigo_estado = models.IntegerField(unique=False, blank=True, null=True, db_column="codigo_estado", verbose_name="codigo_estado", max_length=3)
    campo_notnull = models.CharField(unique=True, blank=False, null=False, db_column="campo_notnull", verbose_name="campo_notnull", )
    pais = models.