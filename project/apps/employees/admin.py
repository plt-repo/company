from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from project.apps.core.utils.admin import get_custom_titled_list_filter
from project.apps.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'father_name', 'position', 'salary', 'age']
    search_fields = ['first_name', 'last_name']
    list_filter = (
        ('position__name', get_custom_titled_list_filter(_('Позиция'))),
    )
