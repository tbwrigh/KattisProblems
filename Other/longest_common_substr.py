n = int(input())

strs = [input() for i in range(n)]

strs = list(sorted(strs, key=len))


for i in range(len(strs[0]), -1, -1):
    is_max = True
    for j in range(len(strs[0])-i):
        is_max = True
        for s in strs:
            if strs[0][j:i+j+1] not in s:
                is_max = False
        if is_max:
            print(i+1)
            exit()

print(0)