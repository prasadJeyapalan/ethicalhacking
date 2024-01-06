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
			
		def buy (self, budget):
			self.budget_check(budget)
			
			if budget >= self.price:
				print(f"You can buy {self.name}")
				
				if budget == self.price:
				
					print("you have just enough money for these shoes")
				else:
					print(f"You can buy these shoes and have $ {self.change(budget)} left over")
				
				exit("Thanks for usng this app")
			else:
				print("Sorry you do not have enough money to buy any shoes")
				
		
		
			
