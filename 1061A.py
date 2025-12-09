t=int(input())
for i in range(t):
    n=int(input())
    ans=0
    while n>2:
        ans+=n//3
        temp=n//3 + n%3
        n=temp
    print(ans)
        