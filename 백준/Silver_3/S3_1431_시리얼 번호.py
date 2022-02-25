import sys

def cSum(str):
    num = 0
    for i in str:
        if i.isdigit():
            num += int(i)
    return num

n = int(sys.stdin.readline())
data = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    data.append([tmp, cSum(tmp), len(tmp)])
data.sort()
data.sort(key= lambda x: x[1])
data.sort(key= lambda x: x[2])
for i in data:
    print(i[0])