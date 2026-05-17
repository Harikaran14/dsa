t=int(input())
for _ in range(t):

    x,y=map(int,input().split())
    modulo=676767677
    need=abs(x-y)
    ans=1
    if need!=1 :
        for i in range(1,int(need**0.5)+1):
            ans=(ans+1) % modulo
    print(ans)
    v=[1]*x
    for i in range(y):
        v.append(-1)
    print(*v)