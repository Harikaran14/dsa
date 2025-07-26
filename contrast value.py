t = int(input())  
for _ in range(t):
    n=int(input())
    x = list(map(int, input().split()) )
    a=x[0]
    tot=0
    c=0
    for i in range(1,n):
        tot +=abs( x[i]-x[i-1])
        if abs(x[i]-a)==tot and i>1 :
            c+=1
        if i==1 and x[1]==a and a!=0:
            c+=1 
    if tot==0 :
        print(1)
    else:            
        print(n-c)        
    