import sys
n = int(sys.stdin.readline())

if n >= 200 :
  print('A')
elif n >= 180 :
  print('B')
elif n >= 150 : 
  print('C')
elif n < 150 :
  print('D')