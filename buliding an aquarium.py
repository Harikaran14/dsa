t = int(input())
for _ in range(t):
    n,x= map(int, input().split())
    a=list(map(int, input().split()))
    l=0
    r=(x//n + 1) + max(a)
    h=l+ (r-l+1)//2
    while l<r:
        total=0
        for i in a:
            total+=max(0,h-i)
        if total<=x:
            l=h
        else:
            r=h-1
        h=l+ (r-l+1)//2  
    print(l)