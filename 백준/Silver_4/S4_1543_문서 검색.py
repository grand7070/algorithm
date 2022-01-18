import sys
data = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
answer = 0
i = 0
while True:
    idx = data.find(target, i)
    if idx == -1: break
    answer += 1
    i = idx + len(target)
print(answer)