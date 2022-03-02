import sys
n = int(sys.stdin.readline())
t = []
p = []
for _ in range(n):
    t_, p_ = map(int, sys.stdin.readline().split())
    t.append(t_)
    p.append(p_)
t.append(0)
p.append(0)
d = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i + t[i] <= n: # 초과 안하면
        print(i, t[i], n)
        d[i] = max(d[i+1], p[i]+d[i+t[i]])
    else:
        d[i] = d[i+1]
    print(d)
print(d[0])