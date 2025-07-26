t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    vs=[0]*n
    d=[]
    for i in range(n):
        d.append([i,x[i]])
    d.sort(key=lambda a:a[1]a[0],reverse=True)    
    ans=0
    for i in d:
        if (i[0]-1 >=0 and vs[i[0]-1]==1) or (i[0]+1<n and vs[i[0]+1]==1):
            pass
        else:
            ans+=1
        vs[i[0]]=1   
    print(ans)    