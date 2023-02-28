s = list(input())

sl = len(s)

ll = []

rl = []

for i in range(sl):
    if len(ll) > 0 and s[i] == "B":
        ll.pop()
    elif len(ll) > 0 and s[i] == "L":
        rl.append(ll.pop())
    elif len(rl) > 0 and s[i] == "R":
        ll.append(rl.pop())
    else:
        ll.append(s[i])

rl = list(reversed(rl))

print("".join(ll) + "".join(rl))