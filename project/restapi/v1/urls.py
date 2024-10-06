from rest_framework import routers

from project.restapi.v1.views import EmployeeViewSet, DepartmentViewSet


api_v1_router = routers.DefaultRouter()
api_v1_router.register(r'employees', EmployeeViewSet)
api_v1_router.register(r'departments', DepartmentViewSet)
