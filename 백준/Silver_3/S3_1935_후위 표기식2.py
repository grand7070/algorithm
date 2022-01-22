import sys
from collections import deque
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpdata = dict()
def change(n):
	return alpdata[n] if n in alpdata.keys() else n
n = int(sys.stdin.readline())
data = deque(list(sys.stdin.readline().rstrip()))
for i in range(n):
	alpdata[alp[i]] = int(sys.stdin.readline())
data = deque(list(map(change, data)))
idx = 0
while len(data) > 1:
	if data[idx] in ['+', '-', '*', '/']:
		tmp = eval(str(data[idx-2])+data[idx]+str(data[idx-1]))
		data[idx-2] = tmp
		del data[idx-1]
		del data[idx-1]
		idx = 0
	else: idx += 1
print(f"{list(data)[0]:.2f}")