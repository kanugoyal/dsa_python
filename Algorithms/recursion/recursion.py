# 1. Divide bigger problem in small and simple problems
# 2. Find a base condition with simple answer
# 3. Return or roll back answer for base condition to solve all sub problems 

def find_sum(n):                  #simple func to sum of 1 to n
    sum
    for i in range(0,n+1):
        sum += i
    return sum


def rec_sum(n):                         #recursive func to sum of 1 to n 
    if n==1:
        return 1
    return n + rec_sum(n-1)

def fib(n):
    #0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index          #creating fibonacci number  with recursion 
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(rec_sum(7))
    print(fib(15))