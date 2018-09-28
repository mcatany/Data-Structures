# Queue

class Queue:
	def __init__(self):
		self.queue = list()
	
	def addtoq(self, dataval):
		if dataval not in self.queue:
			self.queue.insert(0,dataval)
			return True
		return False
		
	def remove(self):
		if self.size() <= 0:
			print("Empty queue")
			return False
			
		return self.queue.pop()
		
	
	def size(self):
		return len(self.queue)
		
aQueue = Queue()
print(aQueue.size())
aQueue.addtoq(1)
print(aQueue.size())
aQueue.addtoq(3)
print(aQueue.size())
aQueue.addtoq(5)		
print(aQueue.size())
print(aQueue.remove())
print(aQueue.size())
print(aQueue.remove())
print(aQueue.size())
print(aQueue.remove())
print(aQueue.size())
