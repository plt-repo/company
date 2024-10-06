from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from project.apps.departments.models import Department
from project.restapi.v1.serializers import DepartmentSerializer


class DepartmentViewSet(ListModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = None
