import math

s=set()
for j in range(2,10**6+1):
    v=1+j
    p=j**2
    for i in range(3,66):
        v+=p
        if v>1e18 :
            break
        s.add(v)
        if p>1e18/j:
            break
        p=p*j

t=int(input())
for _ in range(t):
    n=int(input())
    if n in s:
        print("YES")
    else:
        if 4*n-3<0:
            print("NO")
        else:
            d=math.isqrt(4*n-3)
            if d*d!=4*n-3:
                print("NO")
            else:
                r1=(-1 +d)
                if (r1%2==0 and r1/2>1) :
                    print("YES")
                else:
                    print("NO") 


