t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    y=[]
    ans=0
    for i in range(n):
        if  a[i]<i+1:
            
            l=0
            r=len(y)-1

            while l<=r:
                mid=(l+r)//2
                if y[mid]+1<a[i]:
                    l=mid+1
                else:
                    r=mid-1
            ans+=r+1    
            y.append(i)
    print(ans)

        

