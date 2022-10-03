# Python program to reverse a stack

class Stack:

	
	def __init__(self):
		self.Elements = []
		
	def push(self, val):
		self.Elements.append(val)
	
	def pop(self):
		return self.Elements.pop()

	def empty(self):
		return self.Elements == []
	
	def show(self):
		for val in reversed(self.Elements):
			print(val)


def BottomInsert(s, val):     # insert value at bottom

	if s.empty():

		s.push(val)
	
	else:
		pop_value = s.pop()
		BottomInsert(s, val)
		s.push(pop_value)


def Reverse(s):    # reverse the stack
	if s.empty():
		pass
	else:
		pop_value = s.pop()
		Reverse(s)
		BottomInsert(s, pop_value)



stk = Stack()

stk.push(40)
stk.push(45)
stk.push(30)
stk.push(35)
stk.push(50)

print("Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()
