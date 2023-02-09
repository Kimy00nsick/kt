n = int(input())
k = int(input())
A = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
result = 0
for i in range(n-1, -1, -1) :
  result += k//A[i]
  k %= A[i]

  if k == 0 :
    break
  
print(result)