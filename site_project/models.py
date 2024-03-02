from django.db import models
from django.utils.translation import gettext as _


# Creación de modelos
class Empresa(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=20)

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    def __str__(self):
        return self.nombre


class Area(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=25)
    empresa = models.ForeignKey(Empresa, verbose_name=_(
        "Empresa"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    def __str__(self):
        return self.nombre + ' ' + self.empresa.nombre


class Tipo(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=20)

    class Meta:
        verbose_name = _("Tipo")
        verbose_name_plural = _("Tipos")

    def __str__(self):
        return self.nombre


class Patch(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=20)

    class Meta:
        verbose_name = _("Patch")
        verbose_name_plural = _("Patchs")

    def __str__(self):
        return self.nombre


class Switch(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=20)

    class Meta:
        verbose_name = _("Switch")
        verbose_name_plural = _("Switchs")

    def __str__(self):
        return self.nombre


class Maquina(models.Model):
    ip = models.CharField(_("Ip"), max_length=20)
    area = models.ForeignKey(Area, verbose_name=_(
        "Area"), on_delete=models.CASCADE)
    nombre = models.CharField(_("Nombre"), max_length=20)

    class Meta:
        verbose_name = _("Maquina")
        verbose_name_plural = _("Maquinas")

    def __str__(self):
        return self.nombre


class PuertoSwitch(models.Model):
    switch = models.ForeignKey(Switch, verbose_name=_(
        "Switch"), on_delete=models.CASCADE)
    numero = models.IntegerField(_("Número"))

    class Meta:
        verbose_name = _("PuertoSwitch")
        verbose_name_plural = _("PuertosSwitch")

    def __str__(self):
        return str(self.numero)


class PuertoPatch(models.Model):
    numero = models.IntegerField(_("Número"))
    nombre = models.CharField(_("Nombre"), max_length=20)
    patch = models.ForeignKey(Patch, verbose_name=_(
        "Patch"), on_delete=models.CASCADE)
    puerto_switch = models.ForeignKey(PuertoSwitch, verbose_name=_(
        "Puerto Switch"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("PuertoPatch")
        verbose_name_plural = _("PuertosPatch")

    def __str__(self):
        return self.nombre
