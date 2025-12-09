t = int(input())  
for _ in range(t):
    x,y=map(int, input().split())
    if y>x:
        ans= ((y-1)**2 )
        if y%2==0:
            ans+=x
        else:
            ans+=2*y-x
    else:
        ans=(x-1)**2
        if x%2!=0:
            ans+=y

        else:
            ans+=2*x-y
    print(ans)
