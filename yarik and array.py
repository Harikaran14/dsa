t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dp=[0]
    ans=-float("inf")
    r=0
    while r<n-1:
        if a[r]%2!=a[r+1]%2:
            r+=1
        else:
            dp.append(r)
            while r<n-1 and a[r]%2==a[r+1]%2:
                r+=1
                
            dp.append(r)        
    dp.append(n-1)

    for i in range(len(dp)-1):
        if i%2==0:
            maxend=0
            for k in range(dp[i],dp[i+1]+1):
                if maxend<=0:
                    maxend=a[k]
                else:
                    maxend+=a[k]
                    ans=max(ans,maxend)

    ans=max(ans,max(a))                
    print(ans)                
            






            