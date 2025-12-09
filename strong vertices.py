t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[a[i]-b[i] for i in range(n)]
    m=max(c)
    ans=[]
    for i in range(n):
        if c[i]==m:
            ans.append(i+1)
    print(len(ans))
    print(*ans)

    
    

    