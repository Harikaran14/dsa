t = int(input())
for _ in range(t):
    n,x= map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    s=[0]
    for i in range(n):
        s.append(a[i]+s[i])
    ans=0

    for i in range(1,n+1):
        if s[i]>x:
            break
        ans+=(x-s[i])//i+1
    print(ans)