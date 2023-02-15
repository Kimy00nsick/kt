import sys
n = int(sys.stdin.readline())
a = [None]*n
b = []
for i in range(n) :
  a[i] = int(sys.stdin.readline())
for i in range(0,n) :
  if a[i] == 0 :
    for j in range(i,-1,-1) :
      if a[j] != 0 :
        a[j] = 0 
        break

print(sum(a))