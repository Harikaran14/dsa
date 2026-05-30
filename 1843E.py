t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    q=int(input())
    c=[]
    for i in range(q):
        x=int(input())
        c.append(x)
    ans=-1
    l=1
    r=q
    def valid(mid):
        temp=[0]*(m+1)
        for i in range(mid):
            temp[c[i]]+=1
        for i in range(1,m+1):
            temp[i]+=temp[i-1]
        
        for i in range(n):
            one=temp[a[i][1]]-temp[a[i][0]-1]
            if one>a[i][1]-a[i][0]+1 - one:
                return True
        return False

    while l<=r:
        mid=(l+r)//2
        if valid(mid):
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)
        

        