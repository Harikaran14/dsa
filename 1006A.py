t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=False
    for i in range(0,n-4):
        if a[i]==1 and a[i+1]==0 and a[i+2]==1:
            x=True
            break
    if x:
        print("NO")
    else:
        print("YES")        