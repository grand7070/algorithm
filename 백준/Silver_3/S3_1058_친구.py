import sys

n = int(sys.stdin.readline())
data = dict()
for i in range(1, n+1):
    data[i] = []
    line = list(sys.stdin.readline().rstrip())
    for idx, alp in enumerate(line):
        if alp == "Y":
            data[i].append(idx+1)

answer_list = [0 for _ in range(n+1)]

for key, value in data.items():
    friends = set(value)
    for v in value:
        friends.update(data[v])
    if key in friends:
        friends.remove(key)
    answer_list[key] = len(friends)

print(max(answer_list))