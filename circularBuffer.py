# Circular Buffer

N = 7
queue = [0] * N
head, tail = 0,0

def push(x):
	global tail
	tail = (tail + 1)%N
	queue[tail] = x
	
def size():
	global head, tail
	return (tail - head + N) %N
	
def pop():
	global head
	head = (head + 1)%N
	return queue[head]
	
def empty():
	return head == tail
	
push(7)
print(queue)
push(8)
print(queue)
push(9)
print(queue)
push(10)
print(queue)
pop()
print(queue)