class dsu:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def findP(self,u):
        parent=u
        if u !=self.parent[u]:
            parent=self.findP(self.parent[u])
        return parent
    def union(self,u,v):
        a=self.findP(u)
        b=self.findP(v)
        if a!=b:
            if self.rank[a]>=self.rank[b]:
                self.parent[b]=a
                self.rank[a]+=1
            else:
                self.parent[a]=b
                self.rank[b]+=1
            return True
        return False

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=[]
    for i in range(1,n):
        x.append([i,i-1,max(a[i],a[i-1])])
    x.append([0,n-1,max(a[0],a[n-1])])
    x.sort(key=lambda x: x[2])
    ans=0
    ds=dsu(n)
    for i in x:
        if ds.union(i[0],i[1]):
            ans+=i[2]
    print(ans)
        


    
