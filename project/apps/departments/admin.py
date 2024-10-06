from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from project.apps.core.utils.admin import get_custom_titled_list_filter
from project.apps.departments.models import Department, Position


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'employees_count', 'employees_total_salaries']
    search_fields = ['name']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = (
        ('department__name', get_custom_titled_list_filter(_('Департамент'))),
    )
