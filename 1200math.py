'''import math
t=int(input())
for _ in range(t):
    n,x,y=list(map(int, input().split()))
    dx=n//x
    dy=n//y
    com=int(n//math.lcm(x,y))
    dx-=com
    dy-=com
    ans=(dx*(2*n + (dx-1)*-1)/2) - (dy*(2+ (dy-1)*1)/2) 
    print(int(ans))    '''

t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int, input().split()))
    d={}
    for i in x:
        if i in x:
            d[i]+=1
        else:
            d[i]=1
    sorted_items = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
    for i in d.keys():
        print(i,end=' ')
        x=i
    print(x+1)
    