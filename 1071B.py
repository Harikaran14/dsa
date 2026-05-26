t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(1,n):
        s+=abs(a[i]-a[i-1])
    diff=float('-inf')
    for i in range(1,n-1):
        diff=max(diff,abs(a[i]-a[i-1])+abs(a[i]-a[i+1])-abs(a[i+1]-a[i-1]))
    diff=max(diff,abs(a[1]-a[0]),abs(a[n-2]-a[n-1]))
    s-=diff
    print(s)

    
    