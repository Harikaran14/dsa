t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ps=[0]*(n+1)
    for i in range(n):
        ps[i+1]=ps[i]+(a[i])
    temp=0
    ans=float('-inf')
    for i in range(0,n):
        ans=max(ans, temp-(ps[n]-ps[i+1]))
        if i==0:
            temp+=a[i]
        else:
            temp+=abs(a[i])
    print(ans)


