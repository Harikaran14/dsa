t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if n==k:
        x=1
        s=0
        for i in range(1,n,2):
            s+=1
            if s!=a[i]:
                break
            x+=1        
    else:
        for i in range(1,n-k+2):
            if a[i]!=1:
                x=1
                break
            else:
                x=2
    print(x)                
            
