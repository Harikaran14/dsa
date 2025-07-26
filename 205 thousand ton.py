
import math 

# method to print the divisors
def printDivisors(n) :
    
    # Note that this loop runs till square root
    i = 1
    l=[]
    while i <= math.sqrt(n):
        
        if (n % i == 0) :
            
            # If divisors are equal, print only one
            if (n / i == i) :
                l.append(i)
            else :
                # Otherwise print both
                l.append(int(n/i))
                l.append(i)
        i = i + 1
    return l 

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=printDivisors(n)
    ans=0
    for x in a:
        maxi=0
        mini=float("inf")
        for i in range(0,n,x):
            temp=sum(l[i:i+x])
            maxi=max(maxi,temp)
            mini=min(mini,temp)
        
        ans=max(ans,(maxi-mini))  
    print(ans)    
        
    
    