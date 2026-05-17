t=int(input())

c=list(map(int,input().split()))
d=list(map(int,input().split()))
dp=[[-1]*(2) for i in range(t+1)]
dp[t][0]=0
dp[t][1]=0
def rec(n,row):
    if dp[n][row]!=-1:
        return dp[n][row]
    take=rec(n+1,row^1)
    if row==0:
        take+=c[n]
    else:
        take+=d[n]
    notake=rec(n+1,row)
    dp[n][row]=max(take,notake)
    return dp[n][row]

print(max(rec(0,0),rec(0,1)))