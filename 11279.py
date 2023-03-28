import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for i in range(n) :
    num = int(sys.stdin.readline())
    arr.append(num)
    
    
def heapsort(iterable) :
    h = []
    
    for i in iterable :
        if i == 0 : 
            if len(h) == 0 : 
                print(0)
            else :
               print(heapq.heappop(h)[1])
        else :
            heapq.heappush(h, (-i, i))
            
heapsort(arr)

    
