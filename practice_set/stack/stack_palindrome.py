#Check whether the given string is Palindrome using Stack

stack = []
top = -1

def push(ele: str):
	global top
	top += 1
	stack[top] = ele

def pop():
	global top
	ele = stack[top]
	top -= 1
	return ele

def isPalindrome(string: str) -> bool:
	global stack
	length = len(string)

	stack = ['0'] * (length + 1)

	mid = length // 2
	i = 0
	while i < mid:
		push(string[i])
		i += 1

	
	if length % 2 != 0:     # Checking if the length of the string is odd, 
		i += 1

	while i < length:
		ele = pop()

		if ele != string[i]:    # characters differ then given string is not a palindrome
			return False
		i += 1
	return True


if __name__ == "__main__":

	string = "malyaylam"
    #string = "madam"
    #string = "kanika"


	if isPalindrome(string):
		print("Yes")
	else:
		print("No")


