ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

day = 0
while True:
    if (ds + day) % ys == 0 and (dm + day) % ym == 0:
        print(day)
        break
    day += 1