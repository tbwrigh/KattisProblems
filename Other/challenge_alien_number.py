n_test_cases = int(input())

def base_change(b10, target):
    max_power = 0
    
    while True:
        if b10 >= len(target) ** (max_power+1):
            max_power += 1
        else:
            break
    
    new_num = ""

    cur_b10 = b10

    for i in range(max_power, -1, -1):
        c = 0
        for j in range(len(target)):
            if cur_b10 >= (len(target) ** i) * j:
                c = j
            else:
                break
        new_num += target[c]
        cur_b10 -= (len(target) ** i) * c
    return new_num

outs = []

for i in range(n_test_cases):
    temp = input().split()
    num = temp[0]
    source_system = temp[1]
    target_system = temp[2]

    base_10_num = 0
    num = list(num)
    num = list(reversed(num))
    num = "".join(num)

    for ci in range(len(num)):
        base_10_num += ( len(source_system) ** ci ) * source_system.index(num[ci])
    
    outs.append(base_change(base_10_num, target_system))


for i in range(len(outs)):
    print(f"Case #{i+1}: {outs[i]}")