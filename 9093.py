import sys

num = int(sys.stdin.readline())
str = [None] * num
arr = []
for i in range(num):
    str = list(sys.stdin.readline().split())
    length = len(str)
    for j in range(length):
      str[j] = str[j][::-1]
    arr.append(str)
for i in range(num):
    result = ' '.join(arr[i])
    print(result)

