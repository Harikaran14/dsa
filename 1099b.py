t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=True
    cur=0
    for i in range(1,n):
        if a[i-1]>a[i]:
            cur=max(a[i-1]-a[i],cur)
    for i in range(1,n):
        if a[i-1]>a[i]:
            a[i]+=cur
            if a[i-1]>a[i]:
                ans=False
                break
        
    if ans:
        print("YES")
    else:
        print("NO")
        
