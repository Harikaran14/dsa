t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    op=0
    aps=[a[0]]
    bb=0
    res=0
    for i in range(0,min(n,k)):
        bb=max(bb,b[i])
        op+=a[i]
        res=max(res,(op+ (bb*(k-i-1))))
    print(res)        



