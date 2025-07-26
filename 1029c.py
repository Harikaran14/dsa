t = int(input())
for _ in range(t):
    n=int(input())
    b= list(map(int, input().split()))
    ans=(n-1)*max(b)
    l=0
    while l<n:
        x=(l-1)*b[l]
        while l<n-1 and b[l+1]==b[l]:
            l+=1
        x+=(n-l)*b[l]
        ans=min(ans,x)
        l+=1
    print(ans)        

