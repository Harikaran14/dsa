t = int(input())  
for _ in range(t):
    n=int(input())
    x=list(map(int, input().split()))
    a=[]
    b=[]
    amax=float('inf')
    bmax=-float('inf')
    
    for i in range(n):
        if i%2==0:
            
            a.append(x[i])
        else:
        
            b.append(x[i])

    ans=sum(a)-sum(b)
    
    print(ans)
