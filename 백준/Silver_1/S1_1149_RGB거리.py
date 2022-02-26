import sys
n = int(sys.stdin.readline())
data = [0, 0, 0]
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for idx, num in enumerate(tmp):
        tmp[idx] = min(num+data[(idx+1)%3], num+data[(idx+2)%3])
    data = tmp[:]
print(min(data))