from math import lcm,gcd
t = int(input())
for _ in range(t):
    n,k=map(int,input().split() )
    a=list(map(int,input().split()))
    x=[]
    for i in range(n):
        x.append([a[i],i])
    x.sort(key= lambda x : (x[0],x[1]))
    y=x[k][0]
    ind=0
    for i in range(n):
        if x[i][0]==y :
            ind=i
            break
    

    
