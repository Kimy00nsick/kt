import sys

tmp = sys.stdin.readline().split()

n = int(tmp[0])
name = tmp[1]

str = sys.stdin.readline().split()

for i in range(0,len(str)) :
    if str[i] == name :
        print(i+1)
