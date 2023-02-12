import sys
num = int(sys.stdin.readline())

a = [None]*num
b = []

for i in range(num) :
  a[i] = int(sys.stdin.readline())

a.sort(reverse = True)

while True :
  if len(a) > 2 and a[0]*a[1] > a[0]+a[1] :
    b.append(a[0]*a[1])
    a = a[2:]
  elif len(a) == 2 and a[0]*a[1] > a[0]+a[1]:
    b.append(a[0]*a[1])
    break
  elif len(a) > 2 and a[0]*a[1] < a[0]+a[1] :
    b.append(a[0])
    a = a[1:]
  elif len(a) == 2 and a[0]*a[1] < a[0]+a[1] : 
    b.append(a[0])
    b.append(a[1])
    break
  elif len(a) == 1 : 
    b.append(a[0])
    break
  
  

print(sum(b))
