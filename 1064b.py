t=int(input())
for _ in range(t):
    a,b,n=map(int,input().split())

    if min(b,a/(n))==b:
                print(1)

    else:
        ans=2
        if a%b==0:
               ans=1
        print(ans)
