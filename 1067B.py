t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x={}
    for i in a:
        x[i]=x.get(i,0)+1

    ans=0
    for k,v in x.items():
        if v==1:
            ans+=1
        elif v%2==0 :
            if a.count(k)!=n:
                ans+=2
            else:
                if n%2!=0:
                    ans+=2
        else:
            ans+=1
    print(ans)
