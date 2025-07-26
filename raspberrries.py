t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=set(map(int, input().split()))
    ans=0
    for i in a:
        ans=min(ans,i%k)
    print(ans)    
        
    
        
    
    