import sys 
S = set()
n = int(sys.stdin.readline())
result = []
def cal(a) :
  b = a.split()
  if b[0] == 'add' :
    S.add(b[1])
  elif b[0] == 'remove' :
    S.discard(b[1])
  elif b[0] == 'check' :
    if b[1] in S :
      result.append(1)
    else :
      result.append(0)
  elif b[0] == 'all' :
    for i in range(1,21):
      S.add(i)
  elif b[0] == 'empty' :
    for i in range(1,21):
      S.discard(i)
    

for i in range(n) :
  a = sys.stdin.readline()
  cal(a)
for i in result :
  print(i)
