t=int(input())
for _ in range(t):
    n,k,b,s=map(int,input().split())
    if k*b<=s<=max(n*(k-1),0):
        ans=[0]*n
        x=0
        for i in range(n):
            if x<b:
                x+=1
                ans[i]+=k
            if i==n-1 and x<b:
                ans[i]+=(b-x)*k
        f=s-(k*b)
        i=0
        while f>0 and i<n:
            if k-1<=f:
                ans[i]+=k-1
                i+=1
                f-=k-1
            else:
                ans[i]+=f
                i+=1
                f-=f
        if sum(ans)!=s:
            print(-1)
        else:    
            for i in ans:
                print(i,end=' ')
            print()    
    
    else:
        print(-1)