import sys
sys.setrecursionlimit(10**5)
n=int(input())
if n%2!=0:
    print(-1)
else:
    adj=[list() for i in range(n+1)]
    for i in range(n-1):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    ans=0
    def rec(n,p):
        global ans
        size=1
        for i in adj[n]:
            if i!=p:
                x=rec(i,n)
                if x%2==0:
                    ans+=1
                else:
                    size+=x
        return size
    rec(1,-1)
    print(ans)

