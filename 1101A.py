t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    #n,c=map(int,input().split())
    d={}
    a.sort()
    s=set(a)
    ans=n
    for j in s:
        left=0
        for i in range(n):
            if a[i]<j:
                left=i+1
            else:
                break
        temp=left
        while temp<n and a[temp]==j:
            temp+=1
        right=n-temp
        ans=min(ans,max(right,left))
    print(ans)        

        
            
