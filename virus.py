t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    y=[]
    for i in range(m-1):
        y.append(a[i+1]-a[i]-1)
    y.append(n-a[m-1]+max(0,a[0]-1))
    x=0
    ans=0
    y.sort(reverse=True)

    for i in range(len(y)):
        val=y[i]-x
        if val >=2:
            x+=4
            ans+=val-1
        elif val==1:
            x+=2
            ans+=1
    print(n-ans)

