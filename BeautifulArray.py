n,x=map(int,input().split())
a=list(map(int,input().split()))
dp=[[0,0,0] for i in range(n+1)]
ans=0

"""
def rec(ind,state,s):
    global ans
    if ind==0:
        if state==2:
            return -float('inf')
        elif state==1:
            movenext= a[ind]*x
        else:
            movenext= a[ind]
            
        if movenext<0:
            movenext=0
        ans=max(ans,movenext)
        return movenext

    if state==2:
        movenext= rec(ind-1,2)+a[ind]
        if movenext<0:
            movenext=0
        makemove=rec(ind-1,1)+a[ind]
        if makemove<0:
            makemove=0
        ans=max(ans,movenext,makemove)
        return (max(movenext,makemove))
    elif state==1:
        movenext= rec(ind-1,1)+a[ind]*x
        if movenext<0:
            movenext=0
        makemove=rec(ind-1,0)+a[ind]*x
        if makemove<0:
            makemove=0
        ans=max(ans,movenext,makemove)
        return (max(movenext,makemove))
    else:
        movenext= rec(ind-1,state)+a[ind]
        if movenext<0:
            movenext=0
        ans=max(ans,movenext)
        return movenext
"""
dp[0][0]=max(a[0],0)
dp[0][1]=max(0,a[0]*x)
dp[0][2]=-float('inf')
ans=max(dp[0][0],dp[0][1])
for ind in range(1,n):
    for state in range(3):
        if state==2:
            movenext= dp[ind-1][2]+a[ind]
            if movenext<0:
                movenext=0
            makemove=dp[ind-1][1]+a[ind]
            if makemove<0:
                makemove=0
            ans=max(ans,movenext,makemove)
            dp[ind][state]=(max(movenext,makemove))
        elif state==1:
            movenext= dp[ind-1][1]+a[ind]*x
            if movenext<0:
                movenext=0
            makemove=dp[ind-1][0]+a[ind]*x
            if makemove<0:
                makemove=0
            ans=max(ans,movenext,makemove)
            dp[ind][state]=max(movenext,makemove)
        else:
            movenext= dp[ind-1][0]+a[ind]
            if movenext<0:
                movenext=0
            ans=max(ans,movenext)
            dp[ind][state]= movenext
print(ans)
            