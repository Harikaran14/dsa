
t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))

    l=x
    r=y-1
    mini=float('inf')
    mid=[]
    ind=None
    for i in range(l,r+1):
        mini=min(mini,a[i])
    for i in range(l,r+1):
        if a[i]==mini:
            ind=i
            temp=i
            while temp<r+1:
                mid.append(a[temp])
                temp+=1
            mid.extend(a[l:i])

    ans=[]
    y=a[:l]+a[r+1:]
    for i in range(len(y)):
        if y[i]>mini:
            ans=y[:i]+mid+y[i:]
            break

    print(*ans)
        
    