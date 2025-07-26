
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=float("inf")
    x=0
    for i in range(n):
        if a[i]<0:
            x+=1
            a[i]=abs(a[i])
        m=min(m,abs(a[i]))
    print(a,x,m)
    if x%2==0:
        print(sum(a))
    else:
        print(sum(a)-2*m)