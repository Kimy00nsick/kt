t = int(input())  #T

def test():
  n = int(input())  #N
  a = [None]*n
  for i in range(0, n):
    a[i] = list(input().split())
  a.sort()
  count = 0
  result = 0
  for i in range(1, n):
    if a[i][1] < a[i-1][1] :
      count += 1
    if count > i-1 :
      result += 1

  return result

for i in range(t):
    print(test())