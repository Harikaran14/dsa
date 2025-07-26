t = int(input())
for _ in range(t):
    n=int(input())
    modo=998244353   
    powers = [0] * (n + 1)

    p= list(map(int, input().split()))
    q= list(map(int, input().split()))
    r=[0]*n
    pmv=0
    qmv=0
    pmaxin=0
    qmaxin=0
    for i in range(n):
        if p[i]>pmv:
            pmv=p[i]
            pmaxin=i
        if q[i]>qmv:
            qmv=q[i]
            qmaxin=i    

        if pmv==qmv: 
            val=(pmv,max( q[i-pmaxin], p[i-qmaxin]) )

        elif pmv>qmv:
            val=(pmv,q[i-pmaxin])
        else:
            val=(qmv,p[i-qmaxin])
        x=0
        for bl in val:
            if powers[bl] ==0:
                powers[bl]=pow(2,bl)
            x+=powers[bl]
        r[i]=x%modo
    print(*r)                  



