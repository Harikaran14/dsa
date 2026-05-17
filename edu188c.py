from math import lcm as gcd
t=int(input())
for _ in range(t):
    a,b,c,m=(map(int,input().split()))
    ans=[m//a*6,m//b*6,m//c*6]
    ans[0]-=3*(m//gcd(a,b))
    ans[0]-=3*(m//gcd(a,c))
    ans[1]-=3*(m//gcd(a,b))
    ans[1]-=3*(m//gcd(c,b))
    ans[2]-=3*(m//gcd(a,c))
    ans[2]-=3*(m//gcd(c,b))
    ans[0]+=2*(m//gcd(a,b,c))
    ans[1]+=2*(m//gcd(a,b,c))
    ans[2]+=2*(m//gcd(a,b,c))
    print(*ans)

