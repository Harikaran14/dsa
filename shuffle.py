t=int(input())
for _ in range(t):
    n,x,m=map(int,input().split())
    c=d=x
    for i in range(m):
        l,r=map(int,input().split())
        if l<=c<=r or l<=d<=r:
            c=min(l,c)
            d=max(d,r)
    print(d-c+1)

    