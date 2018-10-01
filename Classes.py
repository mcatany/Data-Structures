# Classes 
# Uses python3

from abc import ABC, abstractmethod

class Beverage(ABC):
	description = ""
	
	@abstractmethod
	def cost():
		pass

class RedBull(Beverage):
	def cost():
		return 1

# Example of usage
if __name__ == "__main__":				
	beverage = RedBull()