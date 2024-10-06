from decimal import Decimal

from django.db import models
from django.db.models import Count, Sum
from django.utils.translation import gettext_lazy as _

from project.apps.core.utils.models import redis_cached_property


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Название'))

    @property
    @redis_cached_property(60 * 60)
    def employees_count(self) -> int:
        if employees_count := self.positions.aggregate(Count('employees__id')).get('employees__id__count'):
            return employees_count
        return 0

    @property
    @redis_cached_property(60 * 60)
    def employees_total_salaries(self) -> Decimal:
        if employees_total_salaries := self.positions.aggregate(
                Sum('employees__salary')).get('employees__salary__sum'):
            return employees_total_salaries
        return Decimal('0.00')

    employees_count.fget.short_description = _('Количество сотрудников')
    employees_total_salaries.fget.short_description = _('Суммарный оклад по всем сотрудникам')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Департамент')
        verbose_name_plural = _('Департаменты')
        ordering = ["id"]
