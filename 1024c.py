t = int(input())
for _ in range(t):
    n=int(input())
    x=[[0 for i in range(n)] for j in range(n)]
    
    val=n*n - n-n+1 
    for i in range(1,n):
        x[i][0]=val
        val+=1
    for i in range(n):
        x[0][i]=val
        val+=1

    
    val=0
    mid= min (n,n - (n - 2) // 2) 

    for i in range(1,mid):
         
        for j in range (i-1,0,-1):
            x[j][i]=val
            val+=1
        for k in range(i,0,-1):
            x[i][k]=val
            val+=1
    
    print(x)
                    
    y=[[0 for i in range(n)] for j in range(n)]
    mid = min(n,n- (n -2) // 2) 
    for i in range(1):
        for j in range(n):
            y[0][j]=x[i][j]
    
    l=1
    for i in range(n - 1, mid - 1, -1):
        for j in range(n):
            y[l][j]=x[i][j]
        l+=1

    for i in range(1, mid):
        for j in range(n):
            y[l][j]=x[i][j]
        l+=1    
    m=n
    print(y)
    mid = min (m,m - (m - 2) // 2)  
    z=[[0 for i in range(n)] for k in range(n)]
    for k in range(n):
        z[k][0]=y[k][0]
    r=1

    for i in range(n - 1, mid - 1, -1):
        for j in range(n):
            z[j][r]=y[j][i]
        r+=1    
    for i in range(1,mid):
        for k in range(n):
            z[k][r] = y[k][i]
        r+=1          

    for i in z:
        for j in i:
            print(j, end=' ')
        print()



