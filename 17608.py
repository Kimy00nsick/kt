import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n) :
    stack.append(int(sys.stdin.readline()))
result = []
result.append(stack.pop())  
for i in range(n-1) :
    if stack[-1] > result[-1] :
        result.append(stack[-1])
        stack.pop()
    else :
        stack.pop()
        
    
print(len(result))