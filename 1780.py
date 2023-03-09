import sys
n = int(sys.stdin.readline())
p = []
for i in range(n) :
    p.append(list(map(int, sys.stdin.readline().split())))

print(p)