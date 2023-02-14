import sys
num = int(sys.stdin.readline())
num1 = num
num2 = num
a = ['A','B','C','D','E','F']
b = []
c = []

while True :
  b.append(num1%8)
  num1 = num1 // 8
  if num1 == 0 :
    break

while True :
  c.append(num2%16)
  num2 = num2 // 16
  if num2 == 0 :
    break

for i in range(len(c)) :
  if c[i] >= 10 and c[i] <= 15 :
    c[i] = a[c[i]-10]
b.reverse()
c.reverse()
b1 = ''.join(str(s)for s in b)
c1 = ''.join(str(s)for s in c)
print(b1,c1)
  