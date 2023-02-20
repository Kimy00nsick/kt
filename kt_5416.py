import sys

n = int(sys.stdin.readline())
a = [None]*n

for i in range(len(a)) :
  a[i] = int(sys.stdin.readline())

print(sum(a))
  
  