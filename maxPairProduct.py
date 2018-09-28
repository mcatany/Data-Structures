# Uses python3
numbers = input("Enter numbers: ")
numbers = numbers.split()

numbers = [int(x) for x in numbers]

max1=-1
max2=-1

for number in numbers:
	if number > max1:
		max2 = max1
		max1 = number
	elif number > max2:
		max2 = number
print(max1 * max2)		