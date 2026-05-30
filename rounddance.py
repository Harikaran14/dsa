from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    vs=[0]*n
    adj=[set() for i in range(n)]
    for i in range(n):
        adj[i].add(a[i]-1)
        adj[a[i]-1].add(i)
    print(adj)
    cycles=0
    disjoints=0
    for i in range(n):
        if vs[i]==0:
            go=True
            q=deque()
            q.append([i,-1])
            vs[i]=1
            while q:
                x,parent=q.popleft()
                for j in adj[x]:
                    if vs[j]==0:
                        q.append([j,x])
                        vs[j]=1
                    else:
                        if j!=parent:
                            go=False
            

            if go:
                disjoints+=1
            else:
                cycles+=1
    
    print(cycles+min(disjoints,1),cycles+disjoints)