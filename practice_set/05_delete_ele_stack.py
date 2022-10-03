#Delete the middle element of a stack using recursion

class Stack:
    def __init__(self):
        self.items = []
      
    def isEmpty(self):
        return self.items == []
      
    def push(self, item):
        self.items.append(item)
      
    def pop(self):
        return self.items.pop()
      
    def peek(self):
        return self.items[len(self.items)-1]
      
    def size(self):
        return len(self.items)

def deleteMid(st, n, curr) :
    if (st.isEmpty() or curr == n) :
        return

    x = st.peek()    #remove current element
    st.pop()

    deleteMid(st, n, curr+1) #remove other elements

    if (curr != int(n/2)) :
        st.push(x)

if __name__ == '__main__':
    st = Stack()
    st.push('11')
    st.push('9')
    st.push('7')
    st.push('29')
    st.push('2')
    st.push('15')
    st.push('28')

    deleteMid(st, st.size(), 0)

    while (st.isEmpty() == False) :     #loop to print stack 
        p = st.peek()
        st.pop()
        print (str(p) + " ", end="")
 