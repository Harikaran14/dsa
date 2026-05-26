'''t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    a= list(map(int, input().split()))
    a.sort()
    l=0
    r=n-1
    ans=False
    while l<=r and r<n:
        if a[r]-a[l]>k:
            l+=1
        elif a[r]-a[l]==k:
            ans=True
            break
        else:
            r+=1
    if ans:
        print("YES")
    else:
        print("NO")
        '''

s=int(input())
for _ in range(s):
    n=int(input())
    a= list(map(int, input().split()))
    t=0
    for i in a:
        if i==a[-1]:
            t+=1
    ans=0
    t=n-t
    a.reverse()
    x=1
    while x<n:
        if a[x]!=a[0]:
            ans+=1
        else:
            x+=1
            continue
        x*=2

    print(ans)
        
        
        
        