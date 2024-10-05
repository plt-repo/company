from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters

from project.apps.employees.models import Employee


class EmployeeFilter(filters.FilterSet):
    department_id = filters.NumberFilter(field_name="position__department__id", label=_('Id департамента'))

    class Meta:
        model = Employee
        fields = ['last_name']
