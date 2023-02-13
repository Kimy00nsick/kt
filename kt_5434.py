import sys
a = sys.stdin.readline().split()

for i in range(len(a)) :
  if a[i] == 'c' : 
    result = a[:i+1]
    break
    
print(' '.join(result))
    