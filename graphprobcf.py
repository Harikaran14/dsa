
n,m=map(int, input().split())
vs=[0]*(n+1)
dg=[0]*(n+1)
adjl=[[] for j in range(n+1)]
answer=0
def dfs(vertex,vs,stack ):
    vs[vertex]=1
    stack.append(vertex)
    for i in adjl[vertex]:
        dg[i]+=1
        if vs[i]==0:
            dfs(i,vs)


for k in range(m):
    u,v=list(map(int, input().split()))
    adjl[u].append(v)
    adjl[v].append(u)

for _ in range(1,n+1):
    if vs[_]==0:
        stack=[]
        cycle=True
        dfs(_ , vs, stack)
        for a in stack:
            if dg[a]!=2:
                cycle=False
                break
        if cycle:
            answer+=1   
print(answer)
      