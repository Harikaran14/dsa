t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    l=[0]*26
    r=[0]*26
    ll=0
    rr=0
    for i in s:
        k=ord(i)-97
        if r[k]==0:
            rr+=1
        r[k]+=1
        

    for i in s:
        k=ord(i)-97
        if l[k]==0:
            ll+=1    
        l[k]+=1
        r[k]-=1
        if r[k]==0:
            rr-=1
        ans=max(ans,ll+rr)
    print(ans)        
