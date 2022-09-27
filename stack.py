from collections import deque
stack = deque()

stack.append("https://www.cnn.com/")               #inserting value in stack one by one
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)

stack.pop()
print(stack)                                    #deleting value from stack one by one

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)                       #push func insert value in stack
        
    def pop(self):                                     #pop func remove value from a stack
        return self.container.pop()
    
    def peek(self):                      #peek func shows last element from stack doesnt delete it
        return  self.container[-1]
    
    def is_empty(self):                    #checks if stack is empty
        return len(self.container)==0
    
    def size(self):                                #size give size of stack 
        return len(self.container)

    def reverse(self,string):
        n = len(string)
        for i in range(0,n):
            s.push(string[i])
        
        string = ""

        for i in range(0,n):
            string += s.pop()
        return string

        




s = Stack()
s.push(5)
s.push(9)
s.push(34)
s.push(78)
s.push(12)
print(s.is_empty())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.size())

str_rev = input("Enter the string to reverse : ")
revers = s.reverse(str_rev)
print("reversed string : "+ revers)

