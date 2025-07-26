t=int(input())
for _ in range(t):
    w,h,a,b=map(int,input().split())
    x1,y1,x2,y2=map(int,input().split())
    ans=True
    if abs(x2-x1)<a:
        if (y2-y1)%b!=0:
            ans=False
    elif abs(y2-y1)<b:
        if (x2-x1)%a!=0:
            ans=False
    elif (((y2-y1-b)%b!=0) and (x2-x1-a)%a!=0):
        ans=False      
    if ans:
        print("YES")
    else:
        print("NO")                    
