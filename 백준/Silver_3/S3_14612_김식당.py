import sys
n, m = map(int, sys.stdin.readline().split())
tables = dict()
for i in range(n):
	query = sys.stdin.readline().split()
	if query[0] == "order":
		table, time = query[1], query[2]
		tables[query[1]] = query[2]
	elif query[0] == "sort":
		tables = dict(sorted(tables.items(), key = lambda x: (int(x[1]), int(x[0]))))
	elif query[0] == "complete":
		del(tables[query[1]])
	if len(tables) == 0:
		print("sleep")
	else:
		print(*tables.keys())