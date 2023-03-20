import sys
from collections import deque
n = int(sys.stdin.readline())
num = []
result = []
for _ in range(n) :
    a = int(sys.stdin.readline())
    num.append(a)

for i in range(n) :
    result.append(min(num))
    num.remove(min(num))

print(result)