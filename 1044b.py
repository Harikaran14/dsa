t=int(input())
for _ in range(t):
    k=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    ans=0
    for i in range(k):
        if i%2==0:
            ans+=l[i]
    print(ans)