from math import sqrt
n = int(input())
messages=[]
for q in range(n):
    square = list(input())
    ssize = int(sqrt(len(square)))
    squared = [square[i*ssize:(i+1)*ssize] for i in range(ssize)]

    message = ""

    c = ssize - 1
    while c >= 0:
        for row in squared:
            message+=row[c]
        c-=1

    messages.append(message)

print("\n".join(messages))