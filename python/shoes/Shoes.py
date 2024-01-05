class Shoes:
		def __init__(self, name, price):
			self.name = name
			self.price = float(price)
		
		def budget_check(self, budget):
			if not isinstance(budget, (int, float)):
				print("Invalid Entry")
				exit()
		
		def change(self, budget):
			return (budget - self.price)
			
		def buy (self, budget)
			self.budget_check(budget)
			
			if budget >= self.price:
				print(f"You can buy {self.name}")
			else:
				print("you have 
				
