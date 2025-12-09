h=list(map(int, input().split()))
n=len(h)
op=[0]*n
m=[]
s=0
for i in range(n-1):
    if h[i]<=h[i+1]:
        m.append([s,i+1])
        s=i+1
    if i==n-2:
        m.append([s,n-1])
y=len(m)
for i in range(y):
    ans=m[i][1]-m[i][0]
    cur=m[i][1]
    for j in range(i+1,y):
        if m[j][1]>cur:
            ans+=1
            cur=m[j][1]
    
    for i in range(m[i][0],m[i][1]):
        op[j]+=ans
print(m)
for i in range(y):
    ans=0
    cur=m[i][0]
    for j in range(i):
        if m[j][0]>cur:
            ans+=1
            cur=m[j][0]
    
    for i in range(m[i][0],m[i][1]):
        op[j]+=ans
print(op)



