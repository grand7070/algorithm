import sys
data = sys.stdin.readline()
answer = set()
for i in range(1, len(data)+1):
    for j in range(len(data)-i):
        answer.add(data[j:j+i])
print(len(answer))