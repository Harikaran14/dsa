t = int(input())  
for _ in range(t):
    n, m = map(int, input().split()) 
    c=[]
    for i in range(n):
        c.append(list(map(int, input().split())) )
    ans=0
    for i in range(m):
        x=[]
        for j in range(n):
            x.append(c[j][i])
        x.sort()    
        for j in range(0,n):
            ans+= x[j]*(j-n+j+1)
    print(ans)            