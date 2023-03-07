import sys
from collections import deque

arr = list(sys.stdin.readline().strip())
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b = ['+', '-', '*', '/']
num = []   # 피연산자
cal = []   # 연산자
for i in range(len(arr)) :
    if arr[i] in b :
        num = arr[:i]
        cal = arr[i:]
        break

def func (a, b, c) :
    if a == '+' :
        return int(b)+int(c)
    elif a == "-":
        return int(b)-int(c)
    elif a == '*':
        return int(b)*int(c)
    elif a == '/' :
        return int(b)/int(c)
cal = deque(cal)   

while True :
    if len(cal) == 0 or len(num) == 1 :
        break
    else :       
        rs = func(cal[0], num[-2], num[-1])
        num.pop()
        num.pop()
        cal.popleft()
        num.append(rs)
    
print(num)

        