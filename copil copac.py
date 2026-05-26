class DisjointSet:
    # To store the ranks, parents and 
    # sizes of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_v] += 1
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    # Function to implement union by size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    
    def getSize(self, node):
        return self.size[self.findUPar(node)]


t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    d=DisjointSet(n)
    for i in range(n-1):
        e=list(map(int,input().split()))
        d.unionByRank(e[0],e[1])
        d.unionByRank(e[1],e[0])
    print(max(d.rank))

        
    
    

    