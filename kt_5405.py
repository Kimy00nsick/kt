import sys
n = sys.stdin.readline().strip()
a = reversed(n)
print(int(''.join(a)))
result = 0
for i in n :
  result += int(i)

print(result)
