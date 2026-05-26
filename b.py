t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    ans=0
    now=0
    s=[]
    for i in range(n):
        temp=0
        a,b,c=map(int,input().split())
        temp=(b-1)*a
        
        d=temp+a-c
        now+=temp
        s.append([d,a,b,c])
    s.sort(reverse=True)

    if s[0][0]<=0 and now<x:
        print(-1)
    elif now>=x:
        print(0)
    else:
        needed=x-now
        ans=(needed+s[0][0]-1)//s[0][0]
        print(ans)