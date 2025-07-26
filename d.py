t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    a=map(int,input().split())
    c=0
    z={}
    for i in a:
        mdx=(int(i)%x)
        mdy=int(i) %y
        
        if ((x-mdx)%x,mdy) in z:
            c+=z[(x-mdx)%x,mdy]
        z[(mdx,mdy)]=z.get((mdx,mdy),0)+1
    print(c)        