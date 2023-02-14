import sys
a = sys.stdin.readline().strip()
result = 0
for i in range(len(a)) :
  if (65>ord(a[i])or (90<ord(a[i])<97) or ord(a[i])>122 or len(a)>20) :
    result = 0
    break
  else :
    result = 1

if result == 0 : 
  print('I')
else :
  print('P')
  #65-90 97-122