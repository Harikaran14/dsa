
def circ(i,x):
    if i>=len(x):
        return i%len(x)
    else:
        return i
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=[]
    count=0
    for i in range(n):
        s=input()
        ip=list(s)
        x.append(ip)

        
    for i in range(min(n,m)//2):
        y=[]
        for j in x[0]:
            y.append(j)
        

        for k in range(1,n):
            y.append(x[k][m-1])
            x[k].pop(m-1) 

        for j in range(-1,-m+1,-1):
            y.append(x[n-1][j])
        

        for k in range(n-1,0,-1):
            y.append(x[k][0])
            x[k].pop(0)
        
        x.pop(n-1)
        x.pop(0)
        
        n=n-2
        m=m-2
        for i in range(len(y)):
            sec=circ(i+1,y)
            third=circ(i+2,y)
            fourth=circ(i+3,y)
            if y[i]=='1' and y[sec]=='5' and y[third]=='4' and y[fourth]=='3':
                count+=1
    print(count)