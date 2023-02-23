import sys

n = int(sys.stdin.readline().strip())
num = [None]*n
for i in range(n) :
    num[i] = int(sys.stdin.readline().strip())   
num.sort(reverse=True)
num.append(num[0])
print(num)
count = 0
result = []
for i in range(1,num[0]+1) :
    for j in range(n) :
        if num[j]%i == num[j+1]%i :
            count += 1     
    if count == n :
        result.append(i)
        count = 0 
                 
print(result)            
