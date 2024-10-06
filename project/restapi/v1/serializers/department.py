from rest_framework.serializers import ModelSerializer, IntegerField, DecimalField

from project.apps.departments.models import Department


class DepartmentSerializer(ModelSerializer):
    employees_count = IntegerField(read_only=True)
    employees_total_salaries = DecimalField(read_only=True, max_digits=11, decimal_places=2)

    class Meta:
        model = Department
        fields = '__all__'
