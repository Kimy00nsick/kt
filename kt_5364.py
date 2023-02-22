import sys

n = list(map(int, sys.stdin.readline().split()))

a = []  # 1,2,3.. 마을 수 
texi = [None]*n[1]  # 택시 가능 마을과 요금
for i in range (1,n[0]+1) : # 1~마을수 
    a.append(i)
    a.append(i)
b = [None]*n[1]
for i in range (n[1]) :
    texi[i] = sys.stdin.readline().split()

for i in range(n[1]) :  # 택시비만 추출 
    b[i] = texi[i][2]
    
b.sort()    # 택시비 오름차순 정렬 

c = [] # 택시비 오름차순 정렬 후 리스트

for i in range(n[1]):
    for j in range(n[1]):
        if b[i] == texi[j][2] :
            c.append(texi[j])

           
result = 0
for i in range(n[1]):
    a.remove(int(c[i][0]))
    a.remove(int(c[i][1]))
    result += int(c[i][2])

    if len(a) == 2 :
        break            
       
print(result)
        
        
        
    
