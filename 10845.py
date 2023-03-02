import sys
from collections import deque
n = int(sys.stdin.readline())
a = [None]*n
queue = deque()

def push(x) :
    queue.append(x) 
    
def pop() :
    if queue == deque() :
        print(-1)
    else :
        print(queue.popleft())

def size() :
    print(len(queue))

def empty() :
    if queue == deque() :
        print(1)
    else :
        print(0)

def front() :
    if queue == deque() :
        print(-1)
    else :
        print(queue[0])

def back() :
    if queue == deque() :
        print(-1)
    else :
        print(queue[-1])
        
for i in range(n) :
    a[i] = sys.stdin.readline().split()

for i in range(n) :
    if a[i][0] == 'push' :
        push(a[i][1])
    elif a[i][0] == 'pop' :
        pop()
    elif a[i][0] == 'size' :
        size()
    elif a[i][0] == 'empty' :
        empty()
    elif a[i][0] == 'front' :
        front()
    elif a[i][0] == 'back' :
        back()
    
    
        
    