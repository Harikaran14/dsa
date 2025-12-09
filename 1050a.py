t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=set(a)
    y=[]
    for i in range(1,n+1):
        if i not in x:
            y.append(i)
    y.reverse()
    s=0
    d={}
    for i in range(n):
        if a[i]==0:
            a[i]=y[s]
            s+=1
    c=-1
    b=-1
    for i in range(n):
        if a[i] != i+1:
            if c==-1:
                c=i
            b=i
    if c==-1:
        print(0)
    else:
        print(b-c+1)



    '''
    pr=[0]*(n+1)
    x=False
    for i in range(n):
        pr[i+1]=pr[i]+a[i]
    for l in range(1,n-1):
        if x:
            break
        for r in range(l+1,n):
            s1=pr[l]
            s2=pr[r]-pr[l]
            s3=pr[n]-pr[r]
            s1%=3
            s2%=3
            s3%=3
            if s1==s2==s3 or s1!=s2 and s2!=s3:
                print(l,r)
                x=True
                break
    if not x:
        print(0,0)'''
            