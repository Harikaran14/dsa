import heapq
n,k1,k2= map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

x=[]
count=0
for i in range(n):
    heapq.heappush(x,-abs(a[i]-b[i]))
for i in range(k1+k2):
    v=heapq.heappop(x)
    if v==0:
        count+=1
    else:
        v+=1
    heapq.heappush(x,v)
ans=0
if count:
    if count%2==0:
        print(0)
    else:
        print(1)
else:
    for i in x:
        ans+=i**2
    print(ans)

