t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    x=0
    ans=[0]*n
    for i in range(n):
        if a[x]=='L':
            x-=1
        else:
            x+=1
        ans[x]=1
    ans[0]=1
    print(ans.count(1))
