t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d={}
    for i in range(n):
        if a[i] not in d:
            d[a[i]]=[]
        d[a[i]].append(b[i])
    b={}
    s=d.items()
    for i in s:
        i[1].sort()
        b[i[0]]=[]
        temp=0
        for j in i[1]:
             temp+=j
             b[i[0]].append(temp)
    ans=[0]*n
    for k,v in b.items():
        
        x=len(v)
        for i in range(1,n+1):
            if i>x:
                ans[i-1]+=0
            else:
                if x%i==0:
                    ans[i-1]+=v[x-1]
                else:
                    rem=x%i
                    ans[i-1]+=v[x-1]-v[rem-1]
    print(*ans)



