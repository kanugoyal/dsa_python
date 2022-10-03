# Python program to sort a stack using recursion

def sortedInsert(s, element):

	# Base case: Either stack is empty or newly inserted
	# item is greater than top (more than all existing)
	if len(s) == 0 or element > s[-1]:
		s.append(element)
		return
	else:
		temp = s.pop()
		sortedInsert(s, element)
		s.append(temp)             # Put back the top item removed earlier

def sortStack(s):

	if len(s) != 0:
		temp = s.pop()
		sortStack(s)
		sortedInsert(s, temp)

def printStack(s):
	for i in s[::-1]:
		print(i, end=" ")
	print()


if __name__ == '__main__':
	s = []
	s.append(22)
	s.append(4)
	s.append(15)
	s.append(33)
	s.append(10)

	print("Stack: ")
	printStack(s)

	sortStack(s)

	print("\nStack after sorting: ")
	printStack(s)

