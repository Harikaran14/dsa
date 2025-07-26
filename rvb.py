
t = int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    x=[a//(b+1)]*(b+1)
    a-=a//(b+1)*(b+1)
    l=0
    while a!=0:
        x[l]+=1
        l-=1
        a-=1

    s=''
    for i in x[:-1]:
        s+=(i*'R')+'B'
    s+=x[-1]*'R'  
    print(x)  
    print(s)



