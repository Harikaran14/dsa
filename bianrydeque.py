t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    cur=0
    maxi=0
    l=0
    r=0
    while r<n:
        cur+=a[r]
        if cur>s:
            cur-=a[l]
            l+=1
        if cur==s:
            maxi=max(maxi,r-l+1)
        
        r+=1
    print(n-maxi if maxi>0 else -1)
    