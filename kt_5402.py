import sys

n = list(map(int, sys.stdin.readline().split()))
str = list(map(int, sys.stdin.readline().split()))

if n[1] not in str :
    print(-1)
else :
    print(str.index(n[1])+1)