t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.insert(0,1)
    a.sort()
    b.sort()
    y=0
    l=s=0
    r=n-1

    
    while s<n and l<=r:
        if a[l]>=b[s]:
            r-=1
            s+=1
            y+=1
        else:
            l+=1
            s+=1

    a.pop(0)
    def s(a,b):
        a.sort()
        b.sort()
        x=0
        l=s=0
        r=n-1

        
        while s<n and l<=r:
            if a[l]>=b[s]:
                r-=1
                s+=1
                x+=1
            else:
                l+=1
                s+=1
        return x
    e=1
    f=m
    while e<=f:
        mid=(e+f)//2
        if s([mid]+a[::],b) == y :
            e=mid+1
        else:
            f=mid-1
    ans=y*(e-1)+(y+1)*(m-e+1)
    print(ans)
        
