
n,q=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
val=0
x=set()
for i in range(n):
    x.add(i)
for i in range(q):
    b=list(map(int,input().split()))
    if b[0]==1:
        if (b[1]-1) not in x:
            s+=b[2]-val
            x.add(b[1]-1)
        else:
            s+=b[2]-a[b[1]-1]
        a[b[1]-1]=b[2]
    else:
        s=b[1]*n
        val=b[1]
        x=set()
    print(s)