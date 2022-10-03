# Python3 program to reverse a queue
from collections import deque

def reversequeue(queue):
	Stack = []

	while (queue):
		Stack.append(queue[0])
		queue.popleft()

	while (len(Stack) != 0):
		queue.append(Stack[-1])
		Stack.pop()

if __name__ == '__main__':
	queue = deque([17,22,28,32,38,42,48,52,58])

	reversequeue(queue)
	print(queue)


