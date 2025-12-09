t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort()
    ans=0
    alen=0
    for i in b:
        if alen<=n:
            for j in range(alen,min(n,alen+i-1)):
                ans+=a[j]
            alen+=i                   
        else:
            break
    for i in range(alen,n):
        ans+=a[i]
    print(ans)

        

