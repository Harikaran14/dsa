t=int(input())
for _ in range(t):
    n=int(input())
    ans=[]
    vs=[0]*(2**n)
    for i in range(n,0,-1):
        cur=2**i-1
        for j in range(cur,2**n):
            if vs[j]==0 and cur&j==cur:
                ans.append(j)
                vs[j]=1
    for i in range(2**n):
        if i%2==0:
            ans.append(i)   
    print(*ans)

