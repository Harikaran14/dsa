t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[0]*n
    l=0
    r=1
    while l<n or r<n:
        if l==r:
            r+=1
        if r<n and a[l]==a[r] :
            r+=1
        else:
            if r-l==1:
                ans=-1
                break
            ans[l]=r
            l+=1
            while l<r:
                ans[l]=l
                l+=1
    if n==1 or ans==-1:
        print(-1)
    else:
        for i in ans:
            print(i,end=' ')
        print()    


        
        
        
        
    