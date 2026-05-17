t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    k=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d={}
    for i in range(m):
        d[c[i]]=0
    
    for i in k:
        d[c[i-1]]+=1
    
    x=list(d.items())
    x.sort()

    l=0
    r=m-1
    ans=0
    for i in range(len(x)-1,-1,-1):
        if x[i][1]==0:
            continue
        if x[i][0]>x[l][0]:
            ans+=x[l][0]
            l+=1
            ans+=x[i][0]*(x[i][1]-1)
        else:
            ans+=x[i][0]*(x[i][1])
    print(ans)