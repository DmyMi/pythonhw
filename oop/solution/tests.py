import unittest as ut

from depart import Departament, Developer, Designer


class TestSalaries(ut.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.Depart = Departament()
		cls.Depart.hire_manager('Vasil', 'Boss', 777, 3)
		devs = [("Junior", "Dev-H@cker", 1500, 1), ("Middle", "Dev-H@cker", 3000, 3), ("Senior", "Dev-H@cker", 7000, 10)]
		for dev in devs:
			_dev = Developer(*dev)
			cls.Depart.managers[0].hire_employee(_dev)
		designers = (("Junior", "Designer", 777, 1, 1), ("Middle", "Designer", 1700, 3, 1.1), ("Da", "Vinci", 7000, 10, 10))
		for designer in designers:
			_designer = Designer(*designer)
			cls.Depart.managers[0].hire_employee(_designer)
		cls.Depart.hire_manager('Dima', 'Boss2', 1000, 7, [])

	def test_count_of_managers(self):
		managers_count = 0
		for x in self.Depart.managers:
			managers_count += 1
		self.assertEqual(2, managers_count)

	def test_salaries(self):
		self.Depart.pay_salary()

	#def test_B(self):
	#	print("Hello")

ut.main()