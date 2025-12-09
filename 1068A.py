t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=input()
    r=0
    ans=0
    maxi=-1
    while r<n:
        if a[r]=='0':
            if r>maxi:
                ans+=1
            
        else:
            maxi=r+k
        r+=1
    print(ans)