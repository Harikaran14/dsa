t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    mini=0
    acc=0
    ans=True
    x=False
    for i in range(n):
        acc+=a[i]
        if i==n-1:
            if (mini==0 and acc-a[0]>=s and x)or( mini!=0 and acc-mini>=s):
                ans=False
                break
        elif acc-mini>=s:
            ans=False
            break
        if acc==0:
            x=True
        mini=min(mini,acc)
    print("YES" if ans else "NO")
