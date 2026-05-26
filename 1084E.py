
isprime=[1]*(1000000+3)
for i in range(2,1000000+3):
    if isprime[i]:
        for j in range(i*i,1000000+3,i):
            isprime[j]=0

isprime[1]=1

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=True
    for i in range(n-1):
        if a[i]>a[i+1]:
            ans=False
    if ans:
        print("Bob")
        continue
    pf=[-1]*n
    sf=[-1]*n
    for i in range(n):
        if isprime[a[i]]==1:
            pf[i]=a[i]
            sf[i]=a[i]
            continue
    
        for j in range(2,int(a[i]**0.5)+1):
            if isprime[j] and a[i]%j==0:
                if sf[i]==-1:
                    sf[i]=j
                pf[i]=max(pf[i],j)
                if isprime[a[i]//j]:
                    pf[i]=max(pf[i],a[i]//j)

    ans=True

    for i in range(n-1):
        if pf[i]==sf[i] and pf[i]<=sf[i+1]:
            pass
        else:
            ans=False
    if sf[-1]!=pf[-1]:
        ans=False
    if ans:
        print("Bob")
    else:
        print("Alice")
