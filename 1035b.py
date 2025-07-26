t = int(input())  
for _ in range(t):
    n=int(input())
    a,b,x,y= map(int, input().split())
    s=list(map(int, input().split()))
    cmin=float('inf')
    cmax=0
    for i in range(n):
        cmax+=s[i]
    cmin=max(0,2*s[0]-cmax)
    d=((a-x)**2 +(b-y)**2)**0.5
    if d==cmax or cmin<=d<=cmax:
        print("YES")
    else:
        print("NO")