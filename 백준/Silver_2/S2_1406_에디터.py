import sys

stack = list(sys.stdin.readline().rstrip())
tmp_stack = []

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    if line[0] == "P":
        stack.append(line[2])
    elif line[0] == "L" and len(stack) > 0:
        tmp_stack.append(stack.pop())
    elif line[0] == "D" and len(tmp_stack) > 0:
        stack.append(tmp_stack.pop())
    elif line[0] == "B" and len(stack) > 0: # B
        stack.pop()

tmp_stack.reverse()
print("".join(stack+tmp_stack))