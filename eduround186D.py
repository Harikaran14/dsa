def fact(x):
    if x==1 or x==0:
        return 1
    return fact(x-1)*x%998244353

MOD = 998244353

def inv(x):
    return pow(x, MOD-2, MOD)

t=int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    s=sum(a)
    v=(s+n-1)//n
    ans=True
    r=s%n
    t=0
    
    for i in a[1:]:
        if i>v:
            ans=False
        if i==v:
            t+=1
    print(s,v,r,t)
    if ans:
        print(int((fact(r) * inv(fact(t)*fact(r-t)) % 998244353 )*fact(n-t)% 998244353))
    else:
        print(0)