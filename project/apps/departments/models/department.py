from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Название'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Департамент')
        verbose_name_plural = _('Департаменты')
