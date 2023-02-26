import sys
n = int(sys.stdin.readline())
li = [] # li[0] = 편의점까지의 거리, li[1] = 편의점에서 얻을 수 있는 포만감
for i in range (n) :
    a, b = sys.stdin.readline().split()
    li.append([int(a),int(b)])

c, d = map(int, sys.stdin.readline().split()) # c = 전체 거리, d = 남은 포만감
li.append([c,0]) 
count = 0

for i in range(n) :
    if d < li[i+1][0]-li[i][0] :
        d += (li[i][1]-(li[i+1][0]-li[i][0]))
        count += 1
    elif d >= li[i+1][0]-li[i][0] :
        d -= (li[i+1][0]-li[i][0]) 

if d < 0 :
    print(-1)
else :
    li.sort(key = lambda x : -x[1])
    for i in range(n) :
        c -= li[i][1]
        if c <= 0 :
            print(i+1)
            break