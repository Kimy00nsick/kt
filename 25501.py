import sys
n = int(sys.stdin.readline())
count = 1
def recursion(s, l, r, count):
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, count)
s = [None]*n
for i in range(n) :
    s[i] = sys.stdin.readline().strip()
    
for i in range(n) :
    a = isPalindrome(s[i])
    print(list(a)[0], list(a)[1])