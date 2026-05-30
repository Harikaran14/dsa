
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    s=input()
    q=int(input())
    zero=0
    one=0
    for i in range(n):
        if s[i]=='1':
            one^=a[i]
        else:
            zero^=a[i]
    pf=[0]
    next=0
    ans=[]
    for i in range(n):
        next^=a[i]
        pf.append(next)
    for i in range(q):
        x=list(map(int, input().split()))
        if x[0]==1:
            l,r=x[1],x[2]
            change=pf[r]^pf[l-1]
            zero^=change
            one^=change
        else:  
            if x[1]==0:
                ans.append(zero)
            else:
                ans.append(one)
    print(*ans)