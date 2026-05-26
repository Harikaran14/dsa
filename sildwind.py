
n,k=map(int,input().split())
a=list(map(int,input().split()))
l=0
ans=[]
temp=0
while l <n:
    if l<k:
        temp+=a[l]
    else:
        ans.append(temp)
        temp-=a[l-k]
        temp+=a[l]
    l+=1
ans.append(temp)
print(sum(ans)/(n-k+1))
