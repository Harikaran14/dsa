t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    d={}
    x=[]

    for i in range(n):
        s=list(map(int,input().split()))
        for j in s[1:]:
            d[j]=d.get(j,0)+1
        x.append(set(s[1:]))
    flag=False
    for i in range(1,m+1):
        if d.get(i,0)==0:
            print('NO')
            flag=True
    if flag:
        continue
    for i in x:
        temp=d
        for j in i:
            if j in x
