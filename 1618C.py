def gcd(x, y):
    while y:
        x, y = y, x % y
    return x



t=int(input())
for _ in  range(t):
    n=int(input())
    a=list(map(int, input().split()))
    
    x=a[0]
    for i in range(0,n,2):
        x=gcd(x,a[i])

    y=a[1]
    
    for i in range(1,n,2):
        y=gcd(y,a[i])
    flag1=True    
    for i in range(1,n,2):
        if a[i]%x==0:
            flag1=False


    flag2=True
    for i in range(0,n,2):    
        if a[i]%y==0:
            flag2=False

    if flag1 and flag2:
        print(x)

    elif flag2 :
        print(y)

    elif  flag1:
        print(x)

    else:
        print(0)                     





            
        
        
            
            