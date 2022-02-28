import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline())]
for i in range(n-1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for idx, num in enumerate(data):
        if idx == 0:
            tmp[idx] += num
            tmp[idx+1] += num
            before = num
        else:
            tmp[idx] = max(tmp[idx], tmp[idx]-before+num)
            tmp[idx+1] += num
            before = num
    data = tmp
print(max(data))