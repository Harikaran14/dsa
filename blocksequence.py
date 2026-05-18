t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dp=[-1]*n
    def rec(ind):
        if ind==n:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        take=float('inf')
        if ind + a[ind]<n:
            take=rec(ind+a[ind]+1)
        notake=rec(ind+1)+1
        dp[ind]=min(take,notake)
        return min(take,notake)    
    print(rec(0))

