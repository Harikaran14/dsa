t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    A=0
    B=0
    s=False
    ans=-1
    for i in range(n-1,-1,-1):
        if i%2==0 and a[i]^b[i]==1:
            A+=1
            if not s:
                s=True
                ans=0
        elif i%2!=0 and a[i]^b[i]==1:
            B+=1
            if not s:
                s=True
                ans=1
    
    
    if (A+B)%2==0 : 
        print("Tie")
    
    else:
        if ans==0:
            print("Ajisai")
        else:
            print("Mai")

