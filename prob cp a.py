t = int(input())  
for _ in range(t):
    a,b,x,y= map(int, input().split())
    if a-b>1:
        print(-1)
    elif a-b==1 and a%2!=0:
        print(y)
    else:
        if x<=y:
            print((b-a) * x)
        else:
            if a%2==0:
                xo=((b-a+1)//2)
                print(xo*y +(b-a-xo)*x) 
            else:
                xo=((b-a+1)//2)
                print(xo*x +(b-a-xo)*y) 