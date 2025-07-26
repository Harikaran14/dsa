t=int(input())
for _ in range(t):
    n=int(input())
    mini=float("inf")
    x=[]
    for i in range(n):
        m=int(input())
        a=list(map(int, input().split()))
        fm=float("inf")
        sm=float("inf")
        for i in a:
            if i<fm:
                sm=fm
                fm=i
            elif i<sm:
                sm=i
        x.append(sm)
        mini=min(mini,fm)
    ans=sum(x)-min(x)+mini
    print(ans)                
