t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    for i in range(n):
        a=input()
        a=list(a)
        x.append(a)
    ans=0

    for i in range(n//2):
        for j in range(i, n- i-1):
            val1=x[i][j]
            val2=x[j][n-i-1]
            val3=x[n-i-1][n-1-j]
            val4=x[n-j-1][i]
            one=[val1,val2,val3,val4]
            if one.count('1')==1 or one.count('1')==3:
                ans+=1
            elif one.count('1')==2:
                ans+=2
    print(ans) 

