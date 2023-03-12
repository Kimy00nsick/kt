import sys
n = int(sys.stdin.readline())

def draw(n, idx) :
    if n == 1:
        star[idx][idx] = '*'
        return 
    l = 4 * n - 3
    
    for i in range(idx, l + idx) :
        star[idx][i] = '*'
        star[idx+l-1][i] = '*'
        
        star[i][idx] = '*'
        star[i][idx+l-1] = '*'
    
    return draw(n-1, idx+2)

len = 4 * n - 3

star = [[' '] * len for _ in range (len)]

draw(n, 0)

for i in range(len) :
    for j in range(len) :
        print(star[i][j], end='')
    print()
        
    