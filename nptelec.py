
t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        while n%2==0:
            n=n/2
        if n==1:
            print("YES")
        else:
            print("NO")        
    else:    
        print("NO")
    
