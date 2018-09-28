# Classes 
from abc import ABC, abstractmethod

class Beverage(ABC):
	description = ""
	
	@abstractmethod
	def cost():
		pass

class RedBull(Beverage):
	def cost():
		return 1
	
beverage = RedBull()