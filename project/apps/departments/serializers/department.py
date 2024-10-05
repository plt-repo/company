from rest_framework.serializers import ModelSerializer, IntegerField, DecimalField

from project.apps.departments.models import Department


class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'
