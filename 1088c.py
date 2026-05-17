t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    ans=True
    s=set()
    
    for i in range(n):
        if b[i]==-1:
            continue
        if b[i] in s:
            ans=False
            break
        s.add(b[i])
        
    for i in range(n-k):
        if b[i]!=a[i]:
            ans=False
            break
    a.reverse()
    b.reverse()
    for i in range(n-k):
        if b[i]!=a[i]:
            ans=False
            break

    if ans:
        print("YES")
    else:
        print("NO")