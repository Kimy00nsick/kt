import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
# arr.sort()
# limit = []
# if sum(arr) <= m :
#     print(max(arr))
# else :
#     for i in (1, max(arr)+1) :
#         result = 0
#         while result <= m :
#             for j in arr :
#                 if i <= j :
#                     result += i 
#                 elif i > j :
#                     result += j
#             limit.append(i)
        
#     print(max(limit))

start, end = 0, max(arr)
while start <= end :
    mid = (start+end) // 2
    result = 0 
    for i in arr :
        if i >= mid :
            result += mid 
        else :
            result += i 
    if result <= m :
        start = mid + 1
    else :
        end = mid - 1
print(end)