t = int(input())
for _ in range(t):
    n,a,b= map(int, input().split())
    x=list(map(int, input().split()))
    pf=[0]
    next=0
    
    for i in range(n):
        next+=x[i]
        pf.append(next)
    ans=b*pf[n]
    for i in range(n):
        lvalue=a*x[i]+b*x[i]
        rvalue=b*(pf[n]-pf[i+1]-(n-i-1)*x[i])
        ans=min(ans,lvalue+rvalue)
    print(ans)
