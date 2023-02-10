a = list(map(int, input().split()))
n = a[0]
k = a[1]
A = [None]*n
for i in range (n) :
  A[i] = int(input())
  
result = 0
for i in range(n-1, 0, -1) :
  result += k//A[i]
  k = k % A[i]

  if k == 0 :
    break
  
print(result)