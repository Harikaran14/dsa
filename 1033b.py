t = int(input())
for _ in range(t):
    n,s=map(int,input().split())
    ans=0
    for i in range(n):
        dx,dy,x,y=map(int,input().split())
        if  ((y==x and dx==dy) or (x+y==s and dx!=dy) ):
            ans+=1
         
    print(ans)        