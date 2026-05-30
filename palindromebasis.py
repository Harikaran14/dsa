n=40007
dp=[0]*n
dp[0]=1
mod=10**9+7
for i in range(1,n):
    if str(i)==str(i)[::-1]:

        for j in range(i,n):
            dp[j]=(dp[j]+dp[j-i]) %mod
t=int(input())
for _ in range(t):
    n=int(input())
    print(dp[n])

        

