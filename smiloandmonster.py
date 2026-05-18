t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    l=0
    r=n-1
    ans=0
    x=0
    while l<r:
        x+=a[l]
        if x<a[r]:
            ans+=a[l]
            l+=1
        else:
            ans+=a[l]
            a[l]=x-a[r]
            ans-=a[l]
            ans+=1
            r-=1
            x=0
            
    if a[r]!=0:
        if a[r]==1:
            ans+=1
        else:
            ans+=(a[r]-x+1)//2+1
    print(ans)
