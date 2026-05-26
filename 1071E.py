t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    s=input()
    p=list(map(int,input().split()))
    tempx=tempy=0
    for i in range(n):
        if p[i]%2==0:
            if s[i]=='1':
                tempy+=p[i]/2+1

            else:
                tempx+=p[i]/2+1

        else:
            if s[i]=='1':
                tempy+=(p[i]+1)//2
            else:
                tempx+=(p[i]+1)//2

    if tempx<x :
        if '0' in s:
            tempx=x
        elif x+n<=y:
            tempx=x
    if tempy<y :
        if '1' in s:
            tempy=y
        elif y+n<=x:
            tempy=y
    if tempx==x and tempy==y:
        print("YES")
    else:
        print("NO")

