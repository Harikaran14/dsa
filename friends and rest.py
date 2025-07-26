t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=[i-j for i,j in zip(b,a)]
    x.sort(reverse=True)
    l=0
    ans=0
    s=x[l]
    r=n-1
    while l<r:
        s+=x[r]
        if s>=0:
            ans+=1
            l+=1
            s=x[l]
        r-=1       
    print(ans)


