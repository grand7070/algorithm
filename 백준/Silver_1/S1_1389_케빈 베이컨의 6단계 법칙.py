import sys
n, m = map(int, sys.stdin.readline().split())
data = {}
for i in range(1, n+1):
    data[i] = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b not in data[a]:
        data[a].append(b)
    if a not in data[b]:
        data[b].append(a)

answer = []
for i in range(1, n+1):
    visited = [i]
    queue = [i]
    distance = [0]*(n+1)
    while queue:
        i = queue.pop(0)
        for j in data[i]:
            if j not in visited:
                visited.append(j)
                queue.append(j)
                distance[j] = distance[i] + 1
    answer.append(sum(distance))
print(answer.index(min(answer))+1)