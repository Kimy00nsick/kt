n = int(input())
word = [None]*n
num = [None]*n
for i in range(n) :
  word[i] = input()
  num[i] = len(word[i])

dic = dict(zip(word, num))
a = dict(sorted(dic.items()))
result = sorted(a,key=lambda x:dic[x])
for i in range(0, len(result)):
  print (result[i])