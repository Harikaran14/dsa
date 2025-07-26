t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d={}
    for i in range(n):
        if b[i] in d.keys():
            d[b[i]]+=a[i]
        else:
            d[b[i]]=a[i]
    x=list(d.keys())
    x.sort()

    d1={i:d[i] for i in x}

    d=d1
    
    total=p
    n-=1
    for i in d.keys():
        if n==0:
            break
        if i<=p:
            if d[i]<=n:
                total+=d[i]*i 
                n-=d[i]
            else:
                total+=n*i
                n=0
        else: 
            total+=p*n
            n=0
    print(total)


