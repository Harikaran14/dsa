t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=True
    p=[]
    t=[]
    s=a[0]
    for i in a:
        s=min(s,i)
        p.append(s)

    a.reverse()
    s=a[0]
    for i in a:
        s=max(s,i)
        t.append(s)
    t.reverse()

    for i in range(0,n-1):
        if p[i]>t[i+1]:
            ans=False
            break
    if ans==True:
        print("Yes")
    else:
        print("No")
