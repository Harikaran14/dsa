t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x={}
    for i in a:
        x[i]=x.get(i,0)+1

    ans=0
    s=0
    for k,v in x.items():
        if v==1:
            ans+=1
        elif v%2==0 :
            if v%4==0:
                s+=1
            else:
                ans+=2
        else:
            ans+=1
    
    if s%2!=0 and not ans:
        ans-=2
    ans+=2*s
    print(ans)
