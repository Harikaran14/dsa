
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    pf=[0]
    next=0
    for i in range(n):
        next+=b[i]
        pf.append(next)
    add=[0]*n
    count=[0]*n
    for i in range(n):
        l=i
        r=n-1
        prev=pf[l]
        count[l]+=1
        ans=i-1
        while l<=r:
            mid=(l+r)//2
            if pf[mid+1]-prev<=a[i]:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        if ans+1!=n:
            add[ans+1]+=a[i]-(pf[ans+1]-prev)
            count[ans+1]-=1

    for i in range(1,n):
        count[i]+=count[i-1]
        
    for i in range(n):
        add[i]+=count[i]*b[i]
    
    print(*add)
         
