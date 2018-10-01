# Advanced Linked List
# Uses python3

# Base class Node
class Node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None
	
# Base class DoublyLinkedList ( nodes point to previous and next nodes)	
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		
	# Add data elements 
	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		if self.head is not None:
			self.head.prev = newNode
		self.head = newNode
		
	# Inser element in the given position
	def insert(self, prev_node, data):
		newNode = Node(data)
		if prev_node is None:
			return
		newNode.next = prev_node.next
		newNode.prev = prev_node
		if newNode.next is not None:
			newNode.next.prev = newNode
	
	# Print whole tree
	def listprint(self, node):
		while node is not None:
			print(node.data)
			last = node
			node = node.next

# Example of usage
if __name__ == "__main__":					
	dllist = DoublyLinkedList()
	dllist.push(12)
	dllist.push(8)
	dllist.push(62)
	dllist.insert(dllist.head.next, 13)
	dllist.listprint(dllist.head)			