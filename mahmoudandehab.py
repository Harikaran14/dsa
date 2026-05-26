from collections import deque
t=int(input())
adj=[[] for i in range(t+1)]
x=set()
y=set()
for i in range(t-1):
    n,m=map(int,input().split())
    adj[n].append(m)
    adj[m].append(n)

vs=[0]*(t+1)
q=deque()
q.append(1)
vs[1]=1
s=True

while q:
    z=len(q)
    for i in range(z):
        cur=q.popleft()
        if s:
            x.add(cur)
        else: 
            y.add(cur)
        for j in adj[cur]:
            if vs[j]==0:
                q.append(j)
                vs[j]=1
    s= not s


lx=len(x)
ly=len(y)
ans=0
for i in x:
    ans+=ly-len(adj[i])

print(ans)



    