t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    ip=[]
    for i in range(n):
        a=list(map(int,input().split()))
        ip.append(a)
    
    d={}
    for i in range(n):
        for j in range(m):
            disp=[(1,0),(-1,0),(0,1),(0,-1)]
            if ip[i][j] not in d.keys():
                        d[ip[i][j]]=0
                        
            for k in disp:
                x=i+k[0]
                y=j+k[1]
                if 0<= x <n and 0<= y <m and ip[x][y]==ip[i][j]:
                    d[ip[i][j]]=2
                    break
 
    op=0
    maxi=0
    for i in d:
        maxi=max(d[i],maxi)
        op+=d[i]
        if d[i]==0:
            op+=1
    op-=maxi
    if maxi==0:
        op-=1
    print(op)    





