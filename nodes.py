# Nodes

class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextdata = None
		
class SLinkedList:
	def __init__(self):
		self.headval = None
	def atBeginning(self, node):
		tmp = self.headval
		self.headval = node
		self.headval.nextdata = tmp
		
	def atEnd(self,node):
		nextval = self.headval
		while nextval.nextdata:		
			nextval = nextval.nextdata
		nextval.nextdata = node		
		
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextdata
		
list1 = SLinkedList()
list1.headval = Node("Mon")

e2 = Node("Tuesday")
e3 = Node("Wednesday")

list1.headval.nextdata = e2
e2.nextdata = e3
e4 = Node("Sunday")
list1.atBeginning(e4)
e5 = Node("Thursday")
list1.atEnd(e5)
e6 = Node("Friday")
list1.atEnd(e6)
e7 = Node("Saturday")
list1.atBeginning(e7)
list1.listprint()
