t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m=0
    p=[0]*(n+1)
    x=[0]*(n)
    for i in range(n):
        m=max(m,a[i])
        x[i]=m
        p[i+1]=p[i]+a[i]
    ans=0
    for i in b:
        l=0
        r=n-1
        mid=l+(r-l+1)//2
        while l<=r:
            if x[mid]>i:
                r=mid-1
            else:
                l=mid+1
            mid=l+(r-l+1)//2
        print(p[r+1],end=' ')

