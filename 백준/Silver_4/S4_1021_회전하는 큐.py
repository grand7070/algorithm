import sys

n, m = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))

data = [i for i in range(1, n+1)]
cnt = 0
for i in target:
    rd = data.index(i)
    ld = len(data) - rd
    if rd < ld:
        for _ in range(rd):
            data.append(data.pop(0))
        data.pop(0)
        cnt += rd
    else:
        for _ in range(ld):
            data.insert(0, data.pop())
        data.pop(0)
        cnt += ld
