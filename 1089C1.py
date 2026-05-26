
def isprime(number):

    if number <= 1:
        return False 
    if number == 2:
        return True 
    if number % 2 == 0:
        return False  
    limit = int(number**0.5) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False 
            
    return True

from math import gcd,lcm
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    for i in range(1,n-1):
        
        l=gcd(a[i],a[i-1])
        r=gcd(a[i],a[i+1])
        lrlcm=lcm(l,r)
        if l>r and l%r==0 and l<=b[i] and l!=a[i] :
            ans+=1
            print(i,0)
    
        elif r>=l and r%l==0 and r<=b[i] and r!=a[i] :
            ans+=1
            print(i,1)
      
        elif lrlcm<=b[i] and (lrlcm!=a[i] or 2*lrlcm<=b[i]) :
            ans+=1
            print(i,2)

    f=gcd(a[0],a[1])
    bb=gcd(a[n-1],a[n-2])
    if f<=b[0]:
        if f!=a[0] :
            ans+=1
        else:
            a[1]//=f
            e=2
            while e*f<=b[0]:
                if isprime(e) and a[1]%e!=0:
                    ans+=1
                    print('a')
                    break
                e+=1

    

    if bb<=b[n-1] :
        if bb!=a[n-1] :
            ans+=1
        else:
            a[n-2]//=bb
            e=2
            while e*bb<=b[n-1]:
                if isprime(e) and a[n-1]%e!=0:
                    ans+=1
                    print('b')
                    break
                e+=1
  
    print(ans)
    