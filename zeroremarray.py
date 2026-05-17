t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        rem=i%k
        if rem==0:
            continue
        if k-rem not in d:
            d[k-rem]=0
        d[k-rem]+=1
    
    ds=list(d.items())
    if len(ds)==0:
        print(0)
        continue
    ds.sort(key= lambda x:(-x[1],-x[0]) )
    print(k*ds[0][1]-(k-ds[0][0])+1)