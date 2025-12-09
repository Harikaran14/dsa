t = int(input())  
for _ in range(t):
    n=input()
    n=n
    z=0
    z2=float('inf')
    x=0
    x2=float('inf')
    for i in range(len(n)):
        if n[i]=='0':
            z=i
            break
    for i in range(len(n)):
        if n[i]=='5':
            x=i
            break
    for i in range(len(n)):
        if n[i] in ['2','7']:
            z2=i
            break
    for i in range(len(n)):
        if n[i] in ['5','0']:
            x2=i
            break
        
    ans=min(z2-1+z,x2-1+x)
    
    print(ans)
    
            
        
    