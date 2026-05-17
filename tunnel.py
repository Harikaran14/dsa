n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
l=0
r=0
c=set()
while l<n and r<n:
    if a[l]==b[r]:
        l+=1
        r+=1
    else:
        ans+=1
        c.add(b[r])
        r+=1

    while l<n and a[l] in c:
        l+=1

print(ans)
