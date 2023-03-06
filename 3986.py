import sys

n = int(sys.stdin.readline())
a = []
b = []
for i in range(n) :
    a.append(sys.stdin.readline().strip())
result = 0   
for i in range(n) :
    if a[i].count('A')%2 != 0 or a[i].count('B')%2 != 0 :
        continue
    
    while True :
        if a[i][-1] == 'A' :
            b.append(a[i][-1])
            a[i] = a[i][:-1]
            if len(a[i]) != 0 and a[i][-1] == 'A' :
                b.append(a[i][-1])
                a[i] = a[i][:-1]  
        else :
            a[i] = a[i][:-1]           
        # elif a[i][-1] == 'B' :
        #     b.append(a[i][-1])
        #     a[i] = a[i][:-1]
        #     if len(a[i]) != 0 and a[i][-1] == 'B' :
        #         b.append(a[i][-1])
        #         a[i] = a[i][:-1]         
        if len(a[i]) < 1 :
            if b.count('B')%2 == 0 :
                result += 1
            break
    b = []
print(result)