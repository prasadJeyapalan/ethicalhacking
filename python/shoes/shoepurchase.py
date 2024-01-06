#!/bin/python3

from Shoes import Shoes

low = Shoes('Mike', 30)
mid = Shoes('Old Balance', 120)
high= Shoes('Donnons', 500)

try:
	shoe_budget = float(input('What is your shoe budget: '))

except ValueError:
	exit("Please enter a number")
	
for shoes in [high, mid, low]:
	shoes.buy(shoe_budget)
	
