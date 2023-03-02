import sys

n = int(sys.stdin.readline())
num = []
for i in range(n) :
    num.append(int(sys.stdin.readline()))
  
result = []

def fibonacci(a) : 
    if a == 0 :
        result.append(0)
        return 0
    elif a == 1 :
        result.append(1)
        return 1
    else :
        return fibonacci(a-1) + fibonacci(a-2)
    
for i in num :   
    fibonacci(i)
    print(result.count(0), result.count(1))
    result = []
