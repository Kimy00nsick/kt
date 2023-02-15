import sys
a,b,n = map(int,sys.stdin.readline().split())

result = 0
count = 0

if (n-b)%(a-b) == 0 :
  count = (n-b)//(a-b)
else :
  count = (n-b)//(a-b) + 1
print(count)