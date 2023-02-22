import sys

n = int(sys.stdin.readline())

a = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
result = 0

for i in a :
    result += n//i
    n %= i
    if n % i == 0 :
        break
    
print(result)
     