import sys

# n = int(sys.stdin.readline())
# a = [None]*n
# for i in range (n) :
#     a[i] = sys.stdin.readline().split()

# dic = {}   
# for i in range (n) :
#     dic[int(a[i][1])]= a[i][0]
# b = list(dic.keys())
# b.sort(reverse=True)
# for i in range(3) :
#     print(dic[b[i]])
   
    
   
# sorted_dic = sorted(dic.items(), reverse=True)
# print(dic)

# b = []
# for i in range (n) :
#     b.append(int(a[i][1]))
    
# b.sort(reverse=True)
# result = []
# for i in range(3) :
#     for j in range(n) :
#         if str(b[i]) == a[j][1] :
#             result.append(a[j][0])
    
# print(result[0])
# print(result[1])
# print(result[2])

n = int(sys.stdin.readline())
a = []
for i in range(n) :
    name, iq = sys.stdin.readline().split()
    a.append((name, int(iq)))
    a.sort(key = lambda x : -x[1])
for i in range (3) :
    print(a[i][0])
    