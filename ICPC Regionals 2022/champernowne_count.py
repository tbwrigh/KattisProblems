n, k = map(int, input().split())

champ = ""

count = 0

for i in range(1, n+1):
    champ += str(i)
    
    if int(champ) % k == 0:
        count += 1
    
    champ = str(int(champ) % k)

print(count)