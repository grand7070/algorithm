import sys

data = sys.stdin.readline().rstrip()
answer = []
tmp = ""
isIt = False

for d in data:
    if d.isnumeric():
        if not tmp and d == "0": continue
        tmp += d
    else:
        answer.append(tmp)
        tmp = ""
        if d == "-":
            if isIt: answer.append(")")
            answer.append(d)
            answer.append("(")
            isIt = True
        else:
            answer.append(d)

answer.append(tmp)
if isIt: answer.append(")")
answer = "".join(answer)

print(eval(answer))