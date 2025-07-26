t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int , input().split()))
    a.sort()
    sumi=sum(a)-sum(a[n-m:])
    maxi=sumi
    for i in range(0,m): 
        if (2*i)<n and (2*i+1)<n:
            sumi=sumi - a[(2*i)] - a[(2*i)+1]

        sumi+= a[n-m + i]
        maxi=max(maxi,sumi)        
    print(maxi)        
        