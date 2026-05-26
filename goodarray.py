n=int(input())
a= list(map(int, input().split()))
s=sum(a)
d={}
se=set()
for i in a:
    d[i]=d.get(i,0)+1
    se.add(i)
ans=[]

for i in range(n):
    if (s-a[i])%2!=0:
        continue
    if (s-a[i])//2 in se:
        if (s-a[i])//2 ==a[i]:
            if d[a[i]]>=2: 
                ans.append(i+1)
        else:
            ans.append(i+1)
if ans:
    print(len(ans))
    print(*ans)
else:
    print(0)
    print()