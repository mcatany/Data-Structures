# Binary Tree

class Node:

	def __init__(self, data):
	
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):
# Compare the new value with the parent node
		if self.data:
			if data < self.data:
				if self.left:
					self.left.insert(data)
				else:
					self.left = Node(data)
			elif data > self.data:
				if self.right:
					self.right.insert(data)
				else:
					self.right = Node(data)
		else:
			self.data = data

	def findval(self, val):
		if self.data == val:
			print(self.data,"found")
		elif val < self.data:
			if self.left.data == val:
				print(val, "found")
			return self.left.findval(val)
		elif val > self.data:
			if self.right.data == val:
				print(val, "found")
			return self.right.findval(val)
		
# Print the tree
	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data)	
		if self.right:
			self.right.PrintTree()
		
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))

root.PrintTree()