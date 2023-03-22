import sys

a , k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

# for i in range(a-1, 0, -1) :
#     if max(arr[:i+1]) != arr[i] :
#         arr[arr.index(max(arr[:i]))], arr[i] = arr[i], arr[arr.index(max(arr[:i]))]
#         k -= 1 
#     if k == 0 :
#         print(arr[arr.index(max(arr[:i]))], arr[i])

# if k > 0 :
#     print(-1)
   
for i in range(a-1, -0, -1) :
    idx = arr.index(max(arr[:i+1]))
    if idx != i :
        arr[idx], arr[i] = arr[i], arr[idx]
        k -= 1
    if k == 0 :
        print(arr[idx], arr[i])

if k > 0 :
    print(-1)