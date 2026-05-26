t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    c2=0
    c5=0
    x=n
    while x%2==0:
        c2+=1
        x/=2

    while x%5==0:
        c5+=1
        x/=5
    k=1
    while c2<c5 and k*2<=m:
        k*=2
        c2+=1
    while c2>c5 and k*5<=m:
        k*=5
        c5+=1
    while k*10<=m:
        k*=10
    
    k*=m//k
    print(n*k)

    
    