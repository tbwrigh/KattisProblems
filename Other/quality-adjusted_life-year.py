import math
n = int(input())
c = [math.prod(list(map(float,input().split()))) for i in range(n)]
print(sum(c))