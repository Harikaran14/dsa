
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=[]
    for i in range(n):
        x.append([a[i],i])
    x.sort(key=lambda e : (-e[0],-e[1]))
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if x[j][0]-x[i][0]==x[j][1]-x[i][1]:
                ans+=1
    print(ans)
