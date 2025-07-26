t = int(input())
for _ in range(t):
    n,m,a,b= map(int, input().split())
    k=max(n-a,a-1)
    l=max(m-b,b-1)
    x=n-k
    y=m-l
    xval,yval,nval,mval=0,0,0,0
    while n>1:
        nval+=1
        n=(n+1)//2
    while m>1:
        mval+=1
        m=(m+1)//2
    while x>1:
        xval+=1
        x=(x+1)//2
    while y>1:
        yval+=1
        y=(y+1)//2     
    print(min(xval+mval,yval+nval)+1)  







    