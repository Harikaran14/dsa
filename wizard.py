
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(2)
    elif a.count(a[0])==n:
        if n%2==0 and a[0] in (n/2,n/2+1):
            print(1)
        elif n%2!=0 and a[0]==(n+1)//2:
            print(2)
        else:
            print(0)

    else:
        ans1=True
        v=[0 for i in range(n)]
        v[0]=1
        for i in range(1,n):
          
            if a[i-1]-a[i]==1:
                v[i]=1
                v[i-1]=1
            elif a[i-1]-a[i]==-1:
                v[i]=-1
                v[i-1]=-1
            elif a[i-1]-a[i]==0:
                pass
            else:
                ans1=False
                break
        pl=[0]*(n+1)
        pr=[0]*(n+1)


        for i in range(1,n):
            
            if v[i]==0:
                if i+1<n and (v[i+1]==0 or v[i-1]==v[i+1]) :
                    v[i]=-v[i-1]
                elif i+1==n:
                    v[i]=-v[i-1]
                else:
                    ans1=False
                    break
        pr[1]=1
        for i in range(1,n):
            pl[i+1]=pl[i]
            pr[i+1]=pr[i]
            if v[i]==1:
                pr[i+1]+=1
            else:
                pl[i+1]+=1
        for i in range(n):
            if a[i]!=pl[i]+1+(pr[n]-pr[i+1]):
                ans1=False
                break
        ans=0

        if ans1:
            ans+=1
        
        ans1=True
        v=[0 for i in range(n)]
        v[0]=-1
        for i in range(1,n):
            if a[i-1]-a[i]==1:
                v[i]=1
                v[i-1]=1
            elif a[i-1]-a[i]==-1:
                v[i]=-1
                v[i-1]=-1
            elif a[i-1]-a[i]==0:
                pass
            else:
                ans1=False
                break
        pl=[0]*(n+1)
        pr=[0]*(n+1)
 
        for i in range(1,n):
            if v[i]==0:
                if i+1<n and (v[i+1]==0 or v[i-1]==v[i+1]) :
                    v[i]=-v[i-1]
                elif i+1==n:
                    v[i]=-v[i-1]
                else:
                    ans1=False
                    break
        pl[1]=1
        for i in range(1,n):
            pl[i+1]=pl[i]
            pr[i+1]=pr[i]
            if v[i]==-1:
                pl[i+1]+=1
            else:
                pr[i+1]+=1
        for i in range(n):
            if a[i]!=pl[i]+1+(pr[n]-pr[i+1]):
                ans1=False
                break
      
        if ans1:
            ans+=1
        print(ans)
