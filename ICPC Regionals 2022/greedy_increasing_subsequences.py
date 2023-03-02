n = int(input())
l = list(map(int, input().split()))


subsequences = []
min_max = float("INF")

for i in l:
    if i <= min_max:
        subsequences.append([i])
        min_max = i
    else:
        for si in range(len(subsequences)):
            if subsequences[si][-1] < i:
                subsequences[si].append(i)
                if si == len(subsequences) - 1:
                    min_max = i
                break

print(len(subsequences))
for subsequence in subsequences:
    print(" ".join(list(map(str, subsequence))))

