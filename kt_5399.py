import sys

n = int(sys.stdin.readline())
dic = set()

for i in range(n) :
    word = sys.stdin.readline().strip()
    length = len(word)
    dic.add((word, length))

li = list(dic)

li.sort(key = lambda x : (x[1],x[0]))
# li.sort(key = lambda x : x[0])

for i in range(len(li)) :
    print(li[i][0])