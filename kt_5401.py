import sys

n = int(sys.stdin.readline())
a = [1,2]*n
for i in range (2,n) :
    
    a[i] = a[i-1] + a[i-2]
    
print(a[n-1]%796796)