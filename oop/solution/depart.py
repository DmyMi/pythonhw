class Departament(object):

	def __init__(self, managers=[]):
		self.managers = managers

	def pay_salary(self):
		for manager in self.managers:
			manager.give_salary()
			for employee in manager.team:
				employee.give_salary()

	def hire_manager(self, name, sname, salary, exp, team=None):
		new_manager = Manager(name, sname, salary, exp, [] if not team else team)
		self.managers.append(new_manager)


class Employee(object):

	def __init__(self, name, sname, salary, exp):
		self.name = name
		self.sname = sname
		self.base_salary = salary
		self.exp = exp

	def calculate_salary(self):
		salary = self.base_salary
		if self.exp > 5:
			salary = salary * 1.2 + 500
		elif self.exp > 2:
			salary += 200
		return salary

	def _print_salary_msg(self, salary):
		GOT_SALARY = "{0} {1}: got salary: {2}"
		print(GOT_SALARY.format(self.name, self.sname, salary))

	def give_salary(self):
		salary = self.calculate_salary()
		self._print_salary_msg(salary)



class Manager(Employee):

	def __init__(self, name, sname, salary, exp, team=None):
		self.team = [] if not team else team
		super().__init__(name, sname, salary, exp)

	def hire_employee(self, employee: Employee):
		self.team.append(employee)

	def calculate_salary(self):
		salary = super().calculate_salary()
		devs = 0
		for emp in self.team:
			if type(emp) == Developer:
				devs += 1
		if not self.team:
			pass		
		elif devs / len(self.team) > 0.5:
			salary *= 1.1
		elif len(self.team) > 5:
			salary += 200
		elif len(self.team) > 10:
			salary += 300
		return salary

	def give_salary(self):
		self._print_salary_msg(self.calculate_salary())


class Developer(Employee):

	def __init__(self, name, sname, salary, exp):
		super().__init__(name, sname, salary, exp)


class Designer(Employee):

	def __init__(self, name, sname, salary, exp, coeff):
		self.coeff = coeff
		super().__init__(name, sname, salary, exp)
	
	def calculate_salary(self):
		salary = super().calculate_salary() * self.coeff
		return salary

	def give_salary(self):
		self._print_salary_msg(self.calculate_salary())