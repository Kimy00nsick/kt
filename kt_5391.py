import sys

a, b = map(int, sys.stdin.readline().split())

count = 0
while True :
    if abs(a/2-b) >= abs(a-b) :
        count += abs(a-b) 
        break
    if a%2 == 0 :
        a/=2
        count += 1 
    elif a%2 != 0 :
        a-=1
        count += 1
    if (a+1)%2 == b :
        a+=1
        count += 1
print(int(count))
