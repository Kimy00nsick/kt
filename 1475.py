import sys
import math

num = sys.stdin.readline().rstrip()
a = [0]*10

for i in range(10) :
  a[i] = num.count(str(i))

a[6] = math.ceil((a[6]+a[9])/2)
a[9] = 0

print(max(a))