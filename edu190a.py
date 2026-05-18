t=int(input())
for _ in range(t):

    a,b,c=(map(int,input().split()))
    if 3*b<=c:
        print(a*b)
    else:
        ans=a//3*c
        if a%3==1:
            if b<=c:
                ans+=b
            else:
                ans+=c
        elif a%3==2:
            if 2*b<=c:
                ans+=2*b
            else:
                ans+=c
        print(ans)

