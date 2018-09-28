#Fibonacci not recursive
#[1,1,3,5,8,13,21,34,55,...]

def fibonacci(n):
	fib = 0
	a = 1
	b = 1
	for i in range(n):
		if i>1:
			fib = (a + b)%10
			b = a
			a = fib
		else:
			fib = 1
	return fib	
n = int(input("Enter a value: "))	
print(fibonacci(n))