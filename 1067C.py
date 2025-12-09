t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=-float('inf')
    temp=0
    t1=0
    for i in range(n):
        temp+=a[i]
        

        
        if temp<0:
            if k%2!=0 and t1==0:
                t1=1
                temp+=b[i]
        res=max(temp,res)
        if temp<0:
            t1=0
            temp=0

    print(res)

    
