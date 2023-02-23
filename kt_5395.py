import sys
n,m = map(int, sys.stdin.readline().split())
a = []
for i in range(n) :
    a.append(int(sys.stdin.readline()))
a.sort(reverse=True)  
count = 0 
for i in range(len(a)) :
    count += m//a[i]
    m = m%a[i]

if m != 0 : 
    print(-1)
else :
    print(count)
    