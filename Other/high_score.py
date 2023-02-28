n = int(input())

def score(a,b,c):
    return a**2 + b**2 + c**2 + 7*min(a,b,c)

outs = []
for i in range(n):
    a,b,c,d = list(map(int,input().split()))
    if max(a,b,c)+d > 7:
        # incorrect for something
        outs.append(max([score(d+a,b,c),score(a,d+b,c),score(a,b,d+c)]))
    else:
        # too slow
        m = 0
        for j in range(d+1):
            for k in range(d-j+1):
                if (t:=score(a+j, b+k, c+(d-j-k))) > m:
                    m = t
                if (t:=score(a+k, b+j, c+(d-j-k))) > m:
                    m = t
                if (t:=score(a+j, b+(d-j-k), c+k)) > m:
                    m = t
                if (t:=score(a+k, b+(d-j-k), c+j)) > m:
                    m = t
                if (t:=score(a+(d-j-k), b+k, c+j)) > m:
                    m = t
                if (t:=score(a+(d-j-k), b+j, c+k)) > m:
                    m = t
        outs.append(m)

for out in outs:
    print(out)