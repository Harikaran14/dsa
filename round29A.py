t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x==y:
        print(-1)
    elif x<y:
        print(2)
    else:
        
        if y==1:
            print(-1)
        elif x>=y+2:
            print(3)
        else:
            print(-1)

