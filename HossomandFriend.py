t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    d={}
    for i in range(1,n+1):
        d[i]=n

    for i in range(m):
        u,v=map(int,input().split())
        if u>v:
            d[v]=min(d[v],u-1)
        else:
            d[u]=min(d[u],v-1)
    x=list(d.items())
    e={}
    e[n] = d[n]
    for i in range(n-1, 0, -1):
        e[i] = min(d[i], e[i+1])


    ans=0
    for k,v in e.items():
        ans+=v-k+1
    print(ans)
