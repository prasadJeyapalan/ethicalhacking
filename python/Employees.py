class Employees:

	def __init__(self, name, dept, role, salary, years_employed):
		self.name = name
		self.dept = dept
		self.role = role
		self.salary = salary
		self.years_employed = years_employed
		
	def eligible_for_retirement(self):
		if self.years_employed >= 20:
			return True
		else:
			return False
			
