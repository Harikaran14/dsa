t=int(input())
for _ in range(t):
    n,m,k =map(int,input().split())
    ans=1
    l=k-1
    r=n-k
    if l<r:
        k=n+1-k
        l,r=r,l
    a=0
    b=0
    
    while True:
        if b<r and a+b+max(b+1,a)-1<=m:
            b+=1
        if a<l and a+b+max(a+1,b)-1<=m:
            a+=1
        else:
            break
    print(a+b+1)
   