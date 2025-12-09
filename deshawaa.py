a=list(map(int,input().split()))
k=int(input())
n=len(a)
l=0
r=k-1
p=[0]
temp=0
for i in range(1,n):
    temp+=abs(a[i]-a[i-1])
    p.append(temp)
   
ans=float("inf")
while r<n:
    if l==0:
        ans=min(ans,p[n-1]-p[r])
    elif r==n-1:
        ans=min(ans,p[n-1]-p[l-1])
    else:
        ans=min(ans,p[n-1]-(p[r+1]-p[l-1])+abs(a[r+1]-a[l-1]))
    l+=1
    r+=1
print(ans)
    
    

    
