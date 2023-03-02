n,m=list(map(int,input().split()))
t=list(map(int,input().split()))
l=list(map(int,input().split()))
t=list(reversed(sorted(t)))
l=sorted(l)
c=0
for i in t:
   if len(l)>0 and i <= l[-1]:
       l.pop()
       c+=1
print(c)
