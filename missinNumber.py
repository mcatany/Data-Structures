A = [1,2,3,4,6,7,10]

def MissingNumber(A):
	B = list(range(A[0],A[-1]+1))
	A = set(A)
	return list(A^set(B))
print(MissingNumber(A))