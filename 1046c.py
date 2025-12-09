t = int(input())  
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    dp=[0]*(n+1)
    p={}
    for i in range(n):
        p[a[i]]=p.get(a[i],[])
        p[a[i]].append(i)
    c={}
    for i in range(1,n+1):
        b=a[i-1]
        c[b]=c.get(b,0)+1
        dp[i]=dp[i-1]
        if c[b]>=b:
            s=p[b][c[b]-b]
            dp[i]=max(dp[i-1],dp[s]+b)
    print(dp[n])



    
