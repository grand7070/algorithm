import sys
n, m = map(int, sys.stdin.readline().split())
girlG = dict()
for _ in range(n):
	group = sys.stdin.readline().rstrip()
	girlG[group] = []
	for _ in range(int(sys.stdin.readline())):
		girlG[group].append(sys.stdin.readline().rstrip())
	girlG[group].sort()
for _ in range(m):
	data = sys.stdin.readline().rstrip()
	question = int(sys.stdin.readline())
	if question == 0:
		for name in girlG[data]:
			print(name)
	else:
		for key, value in girlG.items():
			if data in value:
				print(key)