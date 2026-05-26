t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if a[1]-a[0]>=a[0]:
        print( a[1]-a[0])
    else:
        print(a[0])