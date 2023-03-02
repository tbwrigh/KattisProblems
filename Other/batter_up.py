n = int(input())
w=0
c = 0
s= list(map(int,input().split()))
for i in range(n):
    t = s[i]
    if t!=-1:
        c+=t
    else:
        w+=1
print(c/(n-w))
