t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    e={}
    f={}
    for i in range(k):
        if c[i] not in e:
            e[c[i]]=[]
        e[c[i]].append(d[i])
        if d[i] not in f:
            f[d[i]]=[]
        f[d[i]].append(c[i])
    ans=0
    for i in range(k):
        ans+=k-(len(e[c[i]])-1)-(len(f[d[i]])-1)-1
    print(ans)
        
        