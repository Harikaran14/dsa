t = int(input())
for _ in range(t):
    n,k,a,b= map(int, input().split())
    x=[]
    for i in range(n):
        s=list(map(int, input().split()))
        x.append(s)
    start=x[a-1]
    end=x[b-1]
    l=float('inf')
    r=float('inf')
    for i in range(k):
        l=min(l,abs(x[i][0]-start[0])+ abs(x[i][1]-start[1]))
        r=min(r,abs(x[i][0]-end[0])+ abs(x[i][1]-end[1]))
    
    ans=l+r
    ans=min(ans,abs(end[0]-start[0])+ abs(end[1]-start[1]))
    print(ans)    


    