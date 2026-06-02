'''
from collections import deque
import math
t=int(input())
for _ in range(t):
    n=int(input())
    q=deque()
    q.append(n)
    ans=0
    s=set()
    while q:
        l=len(q)
        for i in range(l):
            x=q.popleft()
            if x==1 and x not in s:
                s.add(x)
                ans+=1
                continue
            elif x<1:
                continue
            else:
                
                if x not in s:
                    s.add(x)
                    ans+=x*x
                    root1= (-1+math.isqrt(1+4*2*x))//2
                    if root1*(root1+1)//2<x:
                        root1+=1
                    if (root1-1)*root1//2+1==x:
                        q.append(x-root1+1) 
                    elif root1*(root1+1)//2==x:
                        q.append(x-root1)
                    else:
                        q.append(x-root1+1)
                        q.append(x-root1)
                    
    print(ans)'''
n=10**6+7
dp=[[0]*2024 for i in range(2024)]
idx=1
ans=[0]*n
for i in range(1,2024):
    for j in range(1,i+1):
        
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]-dp[i-2][j-1]+idx*idx
        
        if idx>n:
            break
        ans[idx-1]=dp[i][j]
        idx+=1
    if idx>n:
        break

t=int(input())
for _ in range(t):
    n=int(input())
    print(ans[n-1])

            