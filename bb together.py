n,d=map(int,input().split())
p=list(map(int,input().split()))
p.sort(reverse=True)
ans=0
l=0
r=0
for i in p:
    l+=1
    x=(d)//i
    if d%i!=0:
        x+=1
    r+=x-1
    if l+r>n:
        break
    ans+=1
print(ans)    

