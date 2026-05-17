
t=int(input())
for _ in range(t):
    n=int(input())
    s=[]
    for i in range(2):
        ip=input()
        s.append(ip)
    '''
    dp=[-1]*(n)
    def rec(v):
        if v==n or v==n+1:
            return 0
        if dp[v]!=-1:
            return dp[v]
        
        if s[0][v]==s[1][v]:
            col=rec(v+1)
        else:
            col=1+rec(v+1)
        row=float('inf')
        if v+1<n:
            r=0
            if s[0][v]!=s[0][v+1]:
                r+=1
            if s[1][v]!=s[1][v+1]:
                r+=1
            row=r+rec(v+2)
        dp[v]=min(row,col)
        return dp[v]
    '''
    dp=[-1]*(n+2)
    dp[n]=dp[n+1]=0
    for v in range(n-1,-1,-1):
        if s[0][v]==s[1][v]:
            col=dp[v+1]
        else:
            col=1+dp[v+1]
        row=float('inf')
        if v+1<n:
            r=0
            if s[0][v]!=s[0][v+1]:
                r+=1
            if s[1][v]!=s[1][v+1]:
                r+=1
            row=r+dp[v+2]
        dp[v]=min(row,col)
    print(dp[0])