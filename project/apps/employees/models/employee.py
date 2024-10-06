from django.db import models
from django.utils.translation import gettext_lazy as _

from project.apps.departments.models import Position


class Employee(models.Model):
    last_name = models.CharField(max_length=255, db_index=True, verbose_name=_('Фамилия'))
    first_name = models.CharField(max_length=255, db_index=True, verbose_name=_('Имя'))
    father_name = models.CharField(max_length=255, verbose_name=_('Отчество'))
    photo = models.ImageField(upload_to='employees', blank=True, null=True, verbose_name=_('Фото'))
    position = models.ForeignKey(Position, models.CASCADE, related_name='employees', verbose_name=_('Должность'))
    salary = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('Оклад'))
    age = models.IntegerField(verbose_name=_('Возраст'))

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')
        unique_together = [["first_name", "last_name", "father_name", "age", "position"]]
        ordering = ["id"]
