# Fibonacci

number = int(input("Enter fibonacci number: "))

result = list()
ant1 = 0
ant2 = 0
for i in range(1,number+1):
	if i < 3:
		fib = 1
		ant1 = 1
		ant2 = 1
	else:
		fib = ant1 + ant2
		ant1 = ant2
		ant2 = fib
	result.append(fib)
print(result[number-1])
print(result[number-1]%10)