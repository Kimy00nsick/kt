import sys

n = int(sys.stdin.readline())
count = 0
for i in range(1,n+1) :
  if i%5 == 0 :
    count += 1

print(count)
  
  