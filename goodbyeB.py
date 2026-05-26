t=int(input())
for _ in range(t):
    r=input()
    x=[]
    for i in r:
        x.append(i)
    ans=0
    if x[0]=='u':
        x[0]='s'
        ans+=1
    if x[-1]=='u':
        x[-1]='s'
        ans+=1
    for i in range(1,len(x)):
        if x[i]=='u' and x[i-1]=='u':
            x[i]='s'
            ans+=1
    print(ans)
