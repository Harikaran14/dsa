from collections import deque
t=int(input())
for _ in range(t):
    n,m=(map(int,input().split()))
    adj=[list() for i in range(n)]
    for i in range(m):
        u,v=(map(int,input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    vs=[0]*n
    ans=0
    clr=[0]*n
    for i in range(n):
        if vs[i]==0:
            vs[i]=1
            q=deque()
            q.append(i)
            s1=set()
            s0=set()
            cond=True
            s0.add(i)
            while q:
                a=q.popleft()
                for j in adj[a]:
                    if vs[j]==1 :
                        if clr[j]==clr[a]:
                            cond=False
                        continue
                    vs[j]=1
                    clr[j]=(clr[a]+1)%2
                    if clr[j]%2==0:
                        s0.add(j)
                    else:
                        s1.add(j)
                    q.append(j)
            if cond:
                ans+=max(len(s1),len(s0))
    print(ans)                    






 