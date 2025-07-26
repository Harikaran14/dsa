t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=[]
    full=n*m*4
    curx=0
    cury=0

    for i in range(n):
        l=list(map(int,input().split()))
        curx+=l[0]
        cury+=l[1]
        x.append([curx,cury])
    print(x)    
    total_lost=0
    for i in range(len(x)-1):
        j=i+1
        xlost=m-abs( x[i][0]-x[j][0])
        ylost=m-abs( x[i][1]-x[j][1])
        if xlost<m:
            total_lost+=2*xlost
        if ylost<m:
            total_lost+=2*ylost
    print(full-total_lost)            
