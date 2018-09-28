# Maximum Slice Problem Codility

A = [5, -7, 3, 5, -2, 4, -1] 

def slow_max_slice(A): # O(n^3)
	
	n = len(A)
	max_slice = 0
	for i in range(n):
		for j in range(i, n):
			sum = 0
			for k in range(i, j):
				sum += A[k]
			max_slice = max(sum, max_slice)	
	return max_slice		


def prefix_sums(A):
			n = len(A)
			P = [0] * (n + 1)
			for i in range(1, n+1):
				P[i] = A[i-1] + P[i-1]
			return P
	
def quadratic_max_slice(A):	# O(n^2):
	max_slice = 0
	n = len(A)
	P = prefix_sums(A)
	print(P)
	for i in range(n):
		for j in range(i,n):
			sum = 0
			sum = P[j+1] - P[i]
			max_slice = max(max_slice, sum)
	return max_slice	
	
def golden_max_slice(A): # O(n)
	
print(slow_max_slice(A))	
print(quadratic_max_slice(A))		
#print(golden_max_slice(A))	