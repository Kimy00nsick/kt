import sys
n = int(sys.stdin.readline())
ps = []
for i in range (n) :
    ps.append(sys.stdin.readline().strip())
  
for i in range(n) :
    count_right = 0
    count_left = 0
    while len(ps[i]) !=0 :
        if ps[i][-1] == '(' :
            print('NO')
            break
        else :
            while ps[i][-1] == ')' :
                count_right += 1
                ps[i] = ps[i][:-1]
            while ps[i][-1] == '(' :
                count_left += 1
                ps[i] = ps[i][:-1]

                   
    if count_left == count_right :
        print('YES')
    elif count_left != count_right : 
        print('NO')

