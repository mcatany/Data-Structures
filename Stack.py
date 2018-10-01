# Stack
# Uses python3

class Stack:
	def __init__(self):
		self.stack = []
		
	def add(self, dataval):
		if dataval not in self.stack:
			self.stack.append(dataval)
			return True
		else:
			return False
			
	def peek(self):
		return self.stack[0]
		
	def remove(self):
		if len(self.stack)<=0:
			return "No elements in the stack"
		else:
			return self.stack.pop()

# Example of usage
if __name__ == "__main__":					
	AStack = Stack()
	AStack.add("Monday")
	AStack.add("Tuesday")
	AStack.peek()
	print(AStack.peek())
	AStack.add("Wednesday")
	AStack.add("Thursday")
	print(AStack.peek())
	print(AStack.stack)
	print(AStack.remove())
	print(AStack.stack)