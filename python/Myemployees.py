#!/bin/python3

from Employees import Employees

emp1 = Employees("Prasad", "Sales", "Manager", 100000, 23)
emp2 = Employees("Linda", "Marketing", "Clerk", 30000, 5)

print(emp1.name)
print(emp2.role)

print(emp1.eligible_for_retirement())
