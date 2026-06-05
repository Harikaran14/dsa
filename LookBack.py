import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(1,n):
        if a[i]<a[i-1]:
            x= math.ceil(a[i-1]/a[i])
            l=len(bin(x))
            if x&(x-1)==0:
                ans+=l-3
                a[i]*=2**(l-3)
            else:
                ans+=l-2
                ans[i]*=2**(l-2)
    print(ans)