t=int(input())
mod=998244353
for _ in range(t):
    n,m=(map(int,input().split()))
    ans=0
    zero=1+(m)//4
    one= (m+2)//4
    rz=1+(n+1)//4-zero
    ro=(n+3)//4-one
    ans=(rz*zero%mod+ro*one%mod)%mod
    print(ans)
