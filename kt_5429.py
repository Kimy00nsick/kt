import sys
n = int(sys.stdin.readline())
a = []
a.append(n%5)
a.append(n%7)
print(max(a))