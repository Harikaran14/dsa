import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=float('inf')
    d={}
    if a.count(a[0])==n:
        print(0)
        continue
    for i in a:
        if i==1:
            d[2]=d.get(2,0)+1
        while i:
            d[i]=d.get(i,0)+1
            if i==1:
                break
            if i%2!=0:
                i+=1
            else:
                i=i>>1
    x=list(d.items())
    cur=-1
    for i in x:
        if i[1]==n:
            cur=i[0]
            new=0
            for j in a:
                while j!=cur:
                    if j%2!=0:
                        j+=1
                    else:
                        j=j>>1
                    new+=1
            ans=min(ans,new)
    print(int(ans))
 