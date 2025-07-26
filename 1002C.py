t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    op=[]
    for i in range(n):
        a=list(map(int,input().split()))
        x.append(a)
        a.reverse()
        xmax=0
        for s in a:
            if s==1:
                xmax+=1
            else:
                break
        if xmax!=0:
            op.append(xmax)    

    j=1
    op.sort()
    prev=0
    ans=0
    for i in op:
        if j<=i and i!=prev:
            ans+=1
            j+=1
            prev+=1

    if n==1:
        print(1)
    elif ans==n:
        print(n)
    else:
        print(ans+1)  





    


