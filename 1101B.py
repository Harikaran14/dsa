t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mini=a[0]
    sumi=0
    ans=[0]*n
    for i in range(n):
        sumi+=a[i]
        ans[i]=min(mini,sumi//(i+1))
        mini=min(mini,ans[i])
    print(*ans)