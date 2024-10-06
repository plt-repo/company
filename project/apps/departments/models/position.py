from django.db import models
from django.utils.translation import gettext_lazy as _

from project.apps.departments.models import Department


class Position(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Название'))
    department = models.ForeignKey(Department, models.CASCADE, related_name='positions', verbose_name=_('Департамент'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Должность')
        verbose_name_plural = _('Должности')
        unique_together = [["name", "department"]]
        ordering = ["id"]
