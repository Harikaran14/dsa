t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    d={}
    for i in x:
        d[i]=d.get(i,0)+1
    y=[]
    for i in d.values():
        y.append(i)
    y.sort()
    ans=0
    m=len(y)
    for i in range(m):
        ans=max(ans,(m-i)*y[i])
    print(ans)



