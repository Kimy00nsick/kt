import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

result = 0
for i in range(n) :
  if a[i] <= 160 :
    print('I',a[i])
    result += 1
    break
if result == 0 : 
  print('P')
    
    