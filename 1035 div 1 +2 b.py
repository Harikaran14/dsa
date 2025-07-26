t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    if a[0]>a[1]:
        print(a[0]+a[1])
    else:
        print(2*a[0])    