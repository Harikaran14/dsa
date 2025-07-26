

t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=[i for i in range(1,n+1)]
    x=[1 for i in range(1,n+1)]
    
    if m<1*n or m>sum(a):
        print(-1)
    else:
        m-=n
        v=m//(n)
        for i in range(1,n):
            l=min(i,v)
            x[i]+=l
            m-=l
      
        l=0
       
        while m!=0 and l<n:
            if x[l]<l+1:
                dif=l+1-x[l]
                if m>=dif:
                    m-=dif
                    x[l]+=dif
                else:
                    x[l]+=m
                    m=0
            l+=1
        m=max(x)
        print(x)
        print(m)
        d={}
        d[m]=[]
        s=set(x)
        print(s)
        for i in s:
            if i!=m:
                d[m].append(i)
                d[i]=[]
        for i in range(n):
            if x[i]!=i+1:
                d[x[i]].append(i+1)
        print(d)
        for k,v in d.items():
            if k==m:
                for i in v:
                    print(k,i)
            else:
                if len(v)>0:
                    print(k,v[0])
                    for i in range(0,len(v)-1):
                        print(v[i],v[i+1])


            

                







           