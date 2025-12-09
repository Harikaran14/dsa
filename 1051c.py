t=int(input())
for _ in range(t):
    n=int(input())
    b=[]
    for i in range(n-1):
        a=list(map(int,input().split()))
        b.append(a)
    rank=[0]*n
    d={}
    for i in range(1,n+1):
        d[i]=set()
    for i in b:
        if i[2]>=i[3]:
            d.setdefault(i[0],set()).add(i[1])
        else:
            d.setdefault(i[1],set()).add(i[0])
    for i in d.keys():
        y=d[i]
        for j in y:
            x=d[j]

            d.setdefault(i,set()).add(j)

    for i in d.keys():
        rank[len(d[i])]=i
    for i in range(n):
        if rank[i]==0:
            rank[i]=1
    print(*rank)
            
