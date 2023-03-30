import sys

t = int(sys.stdin.readline())

def dp() :
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    d = [[] for _ in range(k+1)]
    for i in range(1, k+1) :
        for j in range(n) :
            d[i].append(0)

    for i in range(n) :
        d[0].append(i+1) 
            
    for i in range(1, k+1) :
        for j in range(n) :
            d[i][j] = sum(d[i-1][:j+1])

    return(d[k][n-1])

result = []
for i in range(t) :
    result.append(dp())

for i in range(t) :
    print(result[i])