t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    pref=[[0 for i in range(32)] for j in range(n)]

    for i in range(n):
        for j in range(32):
            k= 1<<j
            if i==0:
                if k&a[i]!=0:
                    pref[i][j]=1
            else:
                if k&a[i]==0:
                    pref[i][j]=pref[i-1][j]
                else:
                    pref[i][j]=pref[i-1][j]+1
    
    fin=[]
    q=int(input())
    for j in range(q):
        l,k=map(int,input().split())
        low=l-1
        r=n-1
        ans=-1
        while low<=r:
            mid=(low+r)//2
            temp=0
            for s in range(32):
                if pref[mid][s]- (pref[l-2][s] if l > 1 else 0)==mid-l+2:
                    temp|=1<<s
            if temp>=k:
                ans=mid
                low=mid+1
            else:
                r=mid-1
        fin.append(ans+1 if ans!=-1 else -1)
    print(*fin)

            
    