t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    b.sort()
    a=sum(b[n:])-sum(b[1:n]) + b[0] 
    print(a)
    c=[0]*(2*n+1)
    d=1
    for k in b[1:n]:
        c[d]=k
        d+=2
    c[d]=a
    d=0
    for k in b[n:]:
        c[d]=k
        d+=2
    c[d]=b[0]    
        
        
    for k in c:    
        print(k, end=' ')
    print()
    


