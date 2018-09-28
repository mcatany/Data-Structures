# Leader Codility

A =[6,8,4,6,8,6,6]
def slowLeader(A): # O(n^2)
	n = len(A)
	leader = -1
	for k in range(n):
		candidate = A[k]
		count = 0
		for i in range(n):
			if A[i] == candidate:
				count +=1
		if count > n//2:
			leader = candidate
	return leader
	

def fastLeader(A): # (n logn)
		n = len(A)
		candidate = A[n//2]
		A.sort() # O (nlogn)
		leader = -1
		count = 0
		for i in range(n):
			if A[i] == candidate:
				count += 1
		if count > n//2:
			leader = candidate
		
		return leader

def goldenLeader(A): # O(n)
	leader = -1
	candidate = -1
	lst = []
	n = len(A)
	size = 0
	count = 0
	for elem in A:
		if size == 0:
			lst.append(A)
			value = elem
			size +=1
		else:
			if elem != value:
				size -= 1
			else:
				size += 1
	if size > 0:
		candidate = value
	
	for elem in A:
		if elem == candidate:
			count += 1
	
	if count > n//2:
		leader = candidate
	return leader	
		
print(slowLeader(A))	
print(fastLeader(A))
print(goldenLeader(A))