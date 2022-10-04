def nex_great_ele(li):              #iterative method
    for i in range(0, len(li), 1):
        next = -1
        for j in range(i+1, len(li),1):
            if li[i] < li[j]:
                next = li[j]
                break

        print(str(li[i])+ "->"+ str(next))

# stack method
def createStack():
    stack = []
    return stack
 
 
def isEmpty(stack):
    return len(stack) == 0
 
 
def push(stack, x):
    stack.append(x)
 
 
def pop(stack):
    if isEmpty(stack):
        print("stack underflow")
    else:
        return stack.pop()
 

def NGE(li):
    
    element = 0
    next = 0
 
    push(s, li[0])
 
   
    for i in range(1, len(li), 1):
        next = li[i]
 
        if isEmpty(s) == False:
 
            element = pop(s)
 

            while element < next:
                print(str(element) + " -> " + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)
 
            
            if element > next:
                push(s, element)
 
        
        push(s, next)
 
 
    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        print(str(element) + " -> " + str(next))
 
 


if __name__ == '__main__':
    li = [24,54,14,9,10]
    nex_great_ele(li)
    s = createStack()
    NGE(li)
