
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=-float('inf')
    pm=[0]*n
    sm=[0]*n
    pm[0]=a[0]
    maxi=a[0]

    for i in range(1,n):
        pm[i]=max(a[i], pm[i-1]+a[i])
        maxi=max(maxi,pm[i])
     
    sm[n-1]=a[n-1]
    for i in range(n-2,-1,-1):
        sm[i]=max(a[i],sm[i+1]+a[i])


    if k%2==0:
        print(maxi)
    else:
        ans=maxi
        for i in range(n):
            v=a[i]+b[i]
            if i>0:
                v+=max(0,pm[i-1])
            if i<n-1:
                v+=max(0,sm[i+1])
            ans=max(ans,v)
        print(ans)
            
    


    
    
