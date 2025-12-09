t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    z=x.count(0)
    s=sum(x)
    a=s-n+1
    a=min(a,n-z)
    print(a)
