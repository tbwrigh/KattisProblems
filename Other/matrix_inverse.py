outs = []

while True:
    try:
        m = [list(map(int, input().split())) for i in range(2)]
        input()
    except:
        break

    mult = 1 / (m[0][0]*m[1][1] - m[1][0]*m[0][1])

    new_m = [[mult*m[1][1], mult*m[0][1]*-1], [mult*m[1][0]*-1, mult*m[0][0]]]

    new_m = [list(map(int, j)) for j in new_m]

    outs.append(new_m)

for i in range(len(outs)):
    print(f"Case {i+1}:")
    print("\n".join([" ".join(list(map(str,outs[i][j]))) for j in range(2)]))