
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    a=list(s)
    e=['0']*n
    ans=0
    for i in range(1,n+1):
        for j in range(i-1,n,i):
            if a[j]=='0':
                if e[j]=='0':
                    ans+=i
                    e[j]='1'
            if a[j]=='1':
                break       
    print(ans)        