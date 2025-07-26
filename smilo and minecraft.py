t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    totalg=0
    og=[]
    ps=[]
    for i in range(n):
        x=input()
        y=[0]
        z=[]
        temp=0
        for j in range(m):
            z.append(x[j])
            if x[j]=='g':
                temp+=1
                totalg+=1
            y.append(temp)
        og.append(z)
        ps.append(y)
    ans=0
    for i in range(n):
        for j in range(m):
            if og[i][j]=='.':
                blockg=0
                for s in range(max(0,i-k+1),min(n,i+k)):
                    print(s,i,j)
                    print(ps[s][min(m,j+k)],ps[s][max(0,j-k)])
                    blockg+=ps[s][min(m,j+k)]-ps[s][max(0,j-k+1)]

                ans=max(ans,totalg-blockg)
    print(ps)            
    print(ans)        



            




