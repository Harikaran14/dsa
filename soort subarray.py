t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a1=list(map(int,input().split()))
    l=0
    r=n-1
    while a[l]==a1[l]:
        l+=1

    while a[r]==a1[r]:
        r-=1

    while 0<l<n and a1[l-1]<=a1[l]:
        l-=1
    while 0<=r<n-1 and a1[r]<=a1[r+1]:
        r+=1

    if r<=l:
        print(1,n)
    else:
        print(l+1,r+1)    




