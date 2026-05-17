t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=[]
    for i in range(n):
        x.append([a[i],i])
    x.sort(key=lambda a:(-a[0],-a[1]))
    ans=0
    cur=n
    for i in x:
        cur = min(cur,i[1])
        if i[1]==0:
            ans+=1
            break
        if i[1]>cur:
            continue
        ans+=1
    print(ans)
