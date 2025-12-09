t=int(input())
for _ in range(t):
    n,k= map(int, input().split())
    a=list(map(int, input().split()))
    pt=False
    f=[0]*(n+1)
    g=[0]*(n+1)
    a.sort()
    for i in a:
        f[i]+=1
    for i in range(1,n+1):
        g[i]=g[i-1]+f[i]
    for i in range(n,0,-1):
        rem=n-g[min(n,4*i)]
        if pt:
            break

        if i<=n:
            rem+=f[i]
        if 2*i<=n:
            rem+=f[i*2]
        if 3*i<=n:
            rem+=f[i*3]
        if rem>=n-k:
            print(i)
            pt=True
    
             



    
