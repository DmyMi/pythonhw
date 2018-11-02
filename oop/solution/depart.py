class Departament(object):
	def __init__(self, managers):
		self.managers = []

	def pay_salary(self):
		GOT_SALARY = "{name} {sname}: got salary: {salary}"
		for manager in managers:
			salary = manager.salary
			print(GOT_SALARY.format(manager.name, manager.sname, salary)

	@staticmethod
	def pay_salary_employeers(employees):
		for emp in employees:
			if (type(emp) == Developer)
				salary = emp.salary()
				print(GOT_SALARY.format(manager.name, manager.sname, salary)
			elif (type(emp) == Designer)
				print(GOT_SALARY.

class Employee(object):
	def __init__(self, name, sname, salary, exp):
		self.name = name
		self.sname = sname
		self.salary = salary
		self.exp = exp

	def got_salary(self)
		salary = self.salary
		if exp > 5:
			salary = salary * 1.2 + 500
		elif exp > 2:
			salary += 200
		return salary


class Manager(Employee):
	def __init__(self, name, sname, salary, exp, team=None: list):
		self.team = team
		super().__init__(name, sname, salary, exp, None)

	def got_salary(self):
		salary = super().get_salary() * self.coeff
		devs = 0
		for emp in manager.team:
			if type(emp) == Developer:
				devs += 1
		if not team:
			pass		
		elif devs / len(manager.team) > 0.5:
			salary *= 1.1
		elif len(manager.team) > 5:
			salary += 200
		elif len(manager.team) > 10:
			salary += 300
		return salary


class Developer(Employee):
	def __init__(self, name, sname, salary, exp):
		super().__init__(name, sname, salary, exp)


class Designer(Employee)
	def __init__(self, name, sname, salary, exp, coeff)
		self.coeff = coeff
		super().__init__(name, sname, salary, exp)
	
	def got_salary(self)
		return super().get_salary() * self.coeff
