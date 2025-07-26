from math import ceil

t=int(input())

for _ in range(t):
    k,a,b,x,y=map(int,input().split())
    ans=0
    ans=max(ans,(k-a)//x+1)    
    ans=max(ans,(k-b)//y+1)
    s=(k-a)//x+1
    newk=k+(s)*-x
    if newk>=b:
        ans=max(ans,s+ceil((newk-b+1)/y))
    s=(k-b)//y+1
    newk=k+(s)*-y
    if newk>=a:
        ans=max(ans,s+ceil((newk-a+1)/x))


    print(ans)
