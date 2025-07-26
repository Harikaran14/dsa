t = int(input())  
for _ in range(t):
    n, k = map(int, input().split()) 
    c=list(map(int, input().split()) )
    s=set(c)
    current={}
    largest={}
    seclargest={}
    for i in s:
        current[i]=0
        largest[i]=-1
        seclargest[i]=-1
    
    for i in range(n):
        d=i-current[c[i]]
        current[c[i]]=i+1
        if largest[c[i]]<d:
            seclargest[c[i]]=largest[c[i]]
            largest[c[i]]=d
        elif seclargest[c[i]]<d:
            seclargest[c[i]]=d
    ans=n
    for i in s:
        d=n-current[i]
        if largest[i]<d:
            seclargest[i]=largest[i]
            largest[i]=d
        elif seclargest[i]<d:
            seclargest[i]=d
    
        ans=min(ans,max(largest[i]//2,seclargest[i]))    
    

    print(ans)