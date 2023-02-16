import sys
n = int(sys.stdin.readline())
a = []
b = []
for i in range(n):
  a.append(sys.stdin.readline().rstrip())

for i in range(n) :
  if a[i].count('g')+a[i].count('G') > a[i].count('b')+a[i].count('B') :
    b.append('is GOOD')
  elif a[i].count('g')+a[i].count('G') < a[i].count('b')+a[i].count('B') :
    b.append('is A BADDY')
  else :
    b.append('is NEUTRAL')


for i in range(n) :
  print(str(a[i]),str(b[i]))