class dsu:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
        
    def fp(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.fp(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        pu=self.fp(u)
        pv=self.fp(v)
        if pv!=pu:
            if self.rank[pv]>self.rank[pu]:
                self.parent[pu]=pv
            elif self.rank[pv]<self.rank[pu]:    
                self.parent[pv]=pu
            else:
                self.parent[pv]=pu
                self.rank[pu]+=1


n,m=map(int, input().split())
edges=[]
answer=0

for i in range(m):
    x=list(map(int, input().split()))
    edges.append(x)
x=[0]*(n+1)
y=set()
vs=[0]*(n+1)
d=dsu(n)
for u,v in edges:
    pu=d.fp(u)
    pv=d.fp(v)
    if pu!=pv:
        d.union(u,v)
    elif pu!=u:
        y.add(pu)
    elif pu==u:
        x[pu]+=1
for a in d.parent[1:]:
    if vs[a]==0:
        vs[a]=1
        if a not in y and x[a]<=1:
            answer+=1
            
print(answer)    