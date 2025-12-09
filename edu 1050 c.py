t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c2=0
    for i in range(1,n):
        if a[i]>=a[i-1] and b[i]>=b[i-1] and a[i]>=b[i-1] and b[i]>=a[i-1]:
            c2+=1

    ans=(2**c2)*2
    print(ans%998244353)

