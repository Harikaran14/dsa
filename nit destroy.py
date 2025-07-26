t = int(input())  
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()) )
    ans=0
    j=0
    while j<n:
        if a[j]!=0:
            ans+=1
            while j<n and a[j]!=0:
                j+=1
        else:
            j+=1
    print(ans)
            
        