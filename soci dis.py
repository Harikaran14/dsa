t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=[]
    x.append(a[0])
    for i in range(1,n-1):
        if a[i-1]<a[i]<a[i+1] or a[i-1]>a[i]>a[i+1]:
            pass
        else:
            x.append(a[i])
    x.append(a[-1])
    print(len(x))
    print(*x)