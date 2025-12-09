t=int(input())
for _ in range(t):
    n=int(input())
    a,b=map(int,input().split())
    if (a-1)%4==0:
        x=a
    elif (a-1)%4==1:
        x=1
    elif (a-1)%4==2:
        x=a+1
    else:
        x=0
    if x==b:
        print(a)
    elif x^b==a:
        print(a+2)
    else:
        print(a+1)

  