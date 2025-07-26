from math import lcm,gcd
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=1
    for i in range(1,n):
        
        y=gcd(a[i-1],a[i])
        y=a[i-1]//y
        x=lcm(x,y)
    print(x)

     