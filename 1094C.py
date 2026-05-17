t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=a[::]
    b.sort()
    mid=b[n//2]
    ps=[0]
    x=0
    ps2=[0]
    y=0
    for i in range(n):
        if a[i]>=mid:
            x+=1 
        else:
            x-=1
        ps.append(x)
        if a[i]<=mid:
            y+=1 
        else:
            y-=1
        ps2.append(y)

#    def rec(i):
 #       if i==0:
  #          return 0
   #     ans=-1
    #    for j in range(i):
     #       if (i-j)%2!=0 and (ps[i]-ps[j])>0:
      #          prev=rec(j)
       #         if prev!=-1:
        #            ans=max(ans,prev+1)
        #return ans
    dp=[-1]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        for j in range(i):
            if dp[j]!=-1 and (i-j)%2!=0 and (ps[i]-ps[j])>0 and (ps2[i]-ps2[j]>0):
                dp[i]=max(dp[i],dp[j]+1)
    print(dp[n])

   