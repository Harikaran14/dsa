n,m=map(int,input().split())
d={}
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        if a[j] not in d:
            d[a[j]]=[]
        d[a[j]].append([i+1,j+1])
ans=0
for k,v in d.items():
    v.sort(key=lambda x : x[0],reverse=True)
    t=len(v)
    temp=t-1
    for i in range(t):
        ans+=temp*v[i][0]
        temp-=2
    v.sort(key=lambda x : x[1],reverse=True)
    t=len(v)
    temp=t-1
    for i in range(t):
        ans+=temp*v[i][1]
        temp-=2
print(ans)
    


    

