n=int(input())
odds=[]
for i in range(1,n+1):
    a=input()
    if i%2==1:
        odds.append(a)
for odd in odds:
    print(odd)