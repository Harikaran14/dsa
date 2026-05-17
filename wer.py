t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        d[i]=1+d.get(i,0)
    d = dict(sorted(d.items(), key=lambda item: item[0], reverse=True))   

    temp=0
    ans=0
    while True:
        for k,v in d.items():
            x=(w-temp)//k
            if x>v:
                temp+=v*k
                d[k]=0
            else:
                temp+=x*k
                d[k]=d[k]-x
        
        if temp==0:
            break
        temp=0
        ans+=1
    print(ans)
        