t=int(input())
for _ in range(t):
    n,x= map(int,input().split())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    c= list(map(int,input().split()))

    d=e=f=True
    ans=False
    t=0
    for i in range(n):
        if d and x|a[i]==x:
            t=t|a[i]
        else:
            d=False
        if e and x|b[i]==x:
            t=t|b[i]
        else:
            e=False
        if f and x|c[i]==x:
            t=t|c[i]
        else:
            f=False
        if t==x:
            ans=True
            break
    if ans:
        print("YES")
    else:
        print("NO")

