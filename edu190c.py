t=int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort(reverse=True)
    one=x.count(1)
    ans=sum(x)-one
    for i in x:
        if one >0 and i!=1:
            v=min(one,i//2 -1)
            ans+=v
            one-=v
    if n-x.count(1)==1 and one>0:
        ans+=1
    if sum(x)<3:
        ans=0
    print(ans)
