import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()
# for i in range(m) :
#     if b[i] not in a :
#         print(0)
#     else :
#         print(1)

for i in b :
    start, end = 0, n-1
    find = False
    while start <= end :
        mid = (start + end) // 2
        if i == a[mid] :
            find = True
            print(1)
            break
        elif i > a[mid] :
            start = mid + 1
        else :
            end = mid - 1

    if not find :
        print(0)