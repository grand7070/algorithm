import sys
from collections import defaultdict

n = int(sys.stdin.readline())
data = defaultdict(list)
for i in range(n):
    root, left, right = sys.stdin.readline().split()
    data[root] = [left, right]

answer = []
def dfs1(key):
    answer.append(key)
    for i in data[key]:
        if i != ".":
            dfs1(i)
dfs1('A')
print("".join(answer))

answer = []
def dfs2(key):
    for i in data[key]:
        if i != ".":
            dfs2(i)
        if key not in answer:
            answer.append(key)
dfs2("A")
print("".join(answer))

answer = []
def dfs3(key):
    for i in data[key]:
        if i != ".":
            dfs3(i)
    answer.append(key)
dfs3("A")
print("".join(answer))
