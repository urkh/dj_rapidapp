from django.db import models


class Tabla1(models.Model):
    tabla5 = models.ForeignKey(Tabla5, blank=True, null=True, verbose_name="tabla5", )


class Tabla2(models.Model):


class Tabla3(models.Model):
    dsfsdfsdf = models.CharField(unique=False, blank=False, null=False, db_column="dsfsdfsdf", verbose_name="dsfsdfsdf", max_length=11)


class Tabla4(models.Model):
    tabla1 = models.ForeignKey(Tabla1, blank=True, null=True, verbose_name="tabla1", )
    tabla2 = models.ForeignKey(Tabla2, blank=True, null=True, verbose_name="tabla2", )


class Tabla5(models.Model):