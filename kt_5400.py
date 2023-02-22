import sys

n = int(sys.stdin.readline())
a = [None]*n
for i in range (n) :
    a[i] = sys.stdin.readline().split()

dic = {}   
for i in range (n) :
    dic[int(a[i][1])]= a[i][0]

sorted_dic = sorted(dic.items(), reverse=True)
print(dic)