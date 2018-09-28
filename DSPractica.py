# DS Práctica

# Nodes

class Daynames:
	def __init__(self, dataval = None):
		self.dataval = dataval
		self.nextval = None
		
day1 = Daynames("Monday")
day2 = Daynames("Tuesday")
day3 = Daynames("Wednesday")

day1.nextval = day2
day2.nextval = day3

#day = day1
#while day != None:
#	print(day.dataval)
#	day = day.nextval
	
# Linked list

class Node:
		def __init__(self, dataval = None):
			self.dataval = dataval
			self.nextval = None
			
class SLinkedList:
	def __init__(self):
		self.headval = None
		
	def printList(self):
		val = self.headval
		while val!=None:
			print(val.dataval)
			val = val.nextval
			
	def atBeginning(self, newVal):
		newNode = Node(newVal)
		newNode.nextval == self.headval
		self.headval = newNode
		
		
		
	
list1 = SLinkedList()
list1.headval = Node("Monday")
day2 = Node("Tuesday")
day3 = Node("Wednesday")
list1.headval.nextval = day2
list1.headval.nextval.nextval = day3
list1.atBeginning("Sunday")

list1.printList()
		