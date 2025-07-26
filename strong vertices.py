t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i!=j and a[i]-a[j]>=b[i]-b[j]:
                x[i].append(j)
    ans=[]
    
    for i in range(n):      
        vs=[0]*n
        q=[]
        q.append(i)
        while len(q)!=0:
            a=q.pop()
            if vs[a]==0:
                for nei in x[a]:
                    q.append(nei)
            vs[a]=1
        if 0 not in vs:
            ans.append(i)
    print(len(ans))
    for i in ans:
        print(i+1,end=' ')
    print()


    
    

    