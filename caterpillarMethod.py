# Caterpillar

def caterpillarMethodMiquel(A,s):
	n = len(A)
	front = 0
	tail = 0
	sum = A[0]
	while sum != s:
		front += 1
		sum += A[front]
		if sum > s:
			sum -= A[tail]
			tail +=1
			
def caterpillarMethod(A, s):
	n = len(A)
	print(A)
	front, total = 0, 0
	for back in range(n):
		while (front < n and total + A[front] <= s):
			print("Back", back,"Front", front, "Total", total)
			total += A[front]
			front += 1
			print("Back", back,"Front", front, "Total", total)
		if total == s:
			return True
		total -= A[back]
	return False	
	
A = [6, 2, 7, 4, 1, 3, 6]

caterpillarMethod(A,12)