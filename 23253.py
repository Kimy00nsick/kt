import sys

n, m = map(int, sys.stdin.readline().split())

a = 0
for i in range(m) :
    int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    if arr !=sorted(arr, reverse=True):
        a = 1
        break
    
if a == 0 :
    print('Yes')
else :
    print('No')
    
    
# import sys

# n, m = map(int, sys.stdin.readline().split())
# stack = [None]*m

# for i in range(m) :
#     k = int(sys.stdin.readline())
#     stack[i] = list(map(int, sys.stdin.readline().split()))
   
# for i in range(n) :
#     for j in range(m) :
#         if len(stack[j]) == 0 :
#             continue
#         if i+1 == stack[j][-1] :
#             stack[j].pop()
# count = 0
# for i in range(m) :
#     if len(stack[i]) == 0 :
#         count += 1

# if count == m :
#     print('Yes')
# else :
#     print('No')