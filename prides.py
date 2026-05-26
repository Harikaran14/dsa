
n=int(input())
ip=[]
for i in range(n):
    x=list(map(int,input().split()))
    ip.append(x)
ip.sort(key=lambda x :(x[0],x[1]))
lp=-1
rp=-1
ans=True
for i in range(n):
    if ip[i][0]>lp:
        lp=ip[i][1]
    elif ip[i][0]>rp:
        rp=ip[i][1]
    else:
        ans=False
        break
if ans:
    print("YES")
else:
    print("NO")
