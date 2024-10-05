from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin

from project.apps.employees.models import Employee
from project.apps.employees.serializers import EmployeeSerializer
from project.apps.employees.filters import EmployeeFilter


class EmployeeViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = EmployeeFilter
