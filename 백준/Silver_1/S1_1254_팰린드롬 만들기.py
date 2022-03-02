import sys
data = list(sys.stdin.readline().rstrip())

def isPel(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def sol(s):
    ans = 0
    while not isPel(s):
        ans += 1
        s = s[1:]
    print(len(data)+ans)
sol(data)