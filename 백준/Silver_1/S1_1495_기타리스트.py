import sys
n, s, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))
volumes = [[False]*(m+1) for _ in range(n)]
before = [False]*(m+1)
before[s] = True
for num, volume in zip(v, volumes):
    for idx, i in enumerate(before):
        if i and idx + num <= m:
            volume[idx + num] = True
        if i and idx - num >= 0:
            volume[idx - num] = True
    before = volume[:]
ans = -1
for idx, i in enumerate(volumes[-1]):
    if i: ans = idx
print(ans)