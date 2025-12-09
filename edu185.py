t = int(input())
for _ in range(t):
    n = int(input())
    maxi=0
    nsq=n*n
    
    for i in range(1,nsq+1):
        c=i
        if 1<=(i-1)<=nsq and (i-1)%n!=0:
            c+=(i-1)
        if 1<=(i+1)<=nsq and (i+1)%n!=1:
            c+=(i+1)
        if 1<=(i-n)<=nsq:
            c+=(i-n)
        if 1<=(i+n)<=nsq:
            c+=(i+n)
        maxi=max(maxi,c)
        
    print(maxi)
