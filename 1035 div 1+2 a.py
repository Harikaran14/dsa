t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=sorted(a)
    x=[]
    for i in range(n):
        if a[i]!=c[i]:
            x.append(a[i])
    if len(x)>0:
        print("YES")
        print(len(x))
        for i in x:
            print(i , end=' ')
        print()
    else:
        print("NO")