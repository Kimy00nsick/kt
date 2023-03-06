import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

num = deque()
result = []
for i in range (n) :
    num.append(i+1)

while len(num) != 0 :
    for i in range(k-1) :
        num.append(num.popleft())
    result.append(num.popleft())
string = list(map(str, result))   
print('<',', '.join(string),'>',sep='')