import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
nums = list(set(data))
nums.sort()
print(nums)
tmp = [0]*n
cnt = 0
for i in nums:
    for j in range(len(data)):
        if i == data[j]:
            tmp[j] = cnt
            cnt += 1
for i in range(len(tmp)):
    print(tmp[i], end=' ')