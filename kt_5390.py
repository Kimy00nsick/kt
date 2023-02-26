import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
a = num.copy()
a.append(0)
result = []
for i in range(n):
    for j in range(i,n) :
        if a[j] < a[j+1] :
            a[j] = 0
        elif a[j] >= a[j+1] :
            a[j+1] = a[j]
    result.append(a.count(0))
    a = num.copy()
    a.append(0)
            
print(max(result)+1)
