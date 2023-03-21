import sys
n = int(sys.stdin.readline())
num = []
for _ in range(n) :
    a = int(sys.stdin.readline())
    num.append(a)

num.sort()
for i in range(n) :
    print(num[i])
# for i in range(n) :
#     result.append(min(num))
#     num.remove(min(num))

# print(result)

# for i in range(n) :
#     min_idx = i
#     for j in range(i+1, n) :
#         if num[min_idx] > num[j] :
#             min_idx = j
#     num[i], num[min_idx] = num[min_idx], num[i]

# for i in range(n) :
#     print(num[i])
