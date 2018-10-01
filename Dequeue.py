# Dequeue (double ended queue)
# Uses python3

from collections import deque

# Example of usage
if __name__ == "__main__":		
	q = deque(["Buffy", "Xander", "Willow"])

	q.append("Giles")

	q.popleft()

	q.pop()

