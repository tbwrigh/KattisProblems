r,f = list(map(int, input().split()))

m = int(round(f / r, 0))

if m % 2 == 0:
    print("up")
else:
    print("down")