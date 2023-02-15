import sys
n = list(map(int,sys.stdin.readline().split()))

if n[0] > 0 and n[1]>0 and n[2]>0 and (sum(n) == 180) :
  print('P')
else :
  print('F')