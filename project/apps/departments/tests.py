from decimal import Decimal

from django.test import TestCase
from django.core.cache import cache

from project.apps.departments.models import Department, Position
from project.apps.employees.models import Employee


class DepartmentModelTests(TestCase):
    def setUp(self):
        department = Department.objects.create(name='test')
        position = Position.objects.create(name='test', department=department)
        Employee.objects.create(
            last_name='test',
            first_name='test',
            father_name='test',
            position=position,
            salary=Decimal('22222.00'),
            age=22
        )

    def tearDown(self):
        cache.clear()

    def test_n_plus_one_problem_in_properties(self):
        """
        Тестируем кэширование результатов model properties
        :return:
        """
        # На один запрос к департаменту запускается еще 2 запроса на расчёт кол-ва сотрудников и сумм окладов
        with self.assertNumQueries(3):
            department = Department.objects.first()
            self.assertEqual(department.employees_count, 1)
            self.assertEqual(department.employees_total_salaries, Decimal('22222.00'))

        # При повторной попытке результат будет получен из кэша
        with self.assertNumQueries(1):
            department = Department.objects.first()
            self.assertEqual(department.employees_count, 1)
            self.assertEqual(department.employees_total_salaries, Decimal('22222.00'))

        # После очистки запросы снова запускаются
        cache.clear()
        with self.assertNumQueries(3):
            department = Department.objects.first()
            self.assertEqual(department.employees_count, 1)
            self.assertEqual(department.employees_total_salaries, Decimal('22222.00'))
