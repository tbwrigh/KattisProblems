n = int(input())
animals = [int(input()) for i in range(n)]
animals = list(sorted(animals))

remains_power = animals.pop()
count = 1
potential_count = 0
potential_power = 0

for i in range(n-1):
    potential_power += animals.pop()
    potential_count += 1

    if potential_power >= remains_power:
        remains_power += potential_power
        count += potential_count
        potential_count = 0
        potential_power = 0
    
print(count)