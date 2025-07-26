def isPrime(j):
    if j==1:
        return False
    for i in range(2,int(j**0.5)+1):
        if j%i ==0:
            return False
    return True
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x={}
    s=set()
    for i in a:
        if isPrime(i):
            x[i]=x.get(i,0)+1
        else:
            for j in range(2,int(i**0.5 ) +1):
                if isPrime(j):
                    while i%j==0 :
                        x[j]=x.get(j,0)+1
                        i=i//j
            if i>1:
                x[i]=x.get(i,0)+1
                
    ans=True
    for k,v in x.items():
        if v%n!=0:
            ans=False
            break

    if (ans and len(x)!=0) or (a.count(a[0])==n) :
        print("YES")
    else:
        print("NO")

#USE SEIVES OF ERASTHONES    
            

 
    
