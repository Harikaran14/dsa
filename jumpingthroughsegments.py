def poss(mid,v):
    ans=True
    l=0
    r=0
    for i in v:
        l=max(l-mid,i[0])
        r=min(r+mid,i[1])
        if l>r:
            return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    v=[]
    for _ in range(n):
        x=list(map(int, input().split()))
        v.append(x)
    
    l=0
    r=1000000000
    mid=(l+r)//2
    while l<r:
        if poss(mid,v):
            r=mid-1
        else:
            l=mid+1
        mid=(l+r)//2
    print(l)