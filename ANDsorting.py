t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    for i in range(n):
        if i!=a[i]:
            s.append(a[i])
    ans=None
    for i in range(1,len(s)):
        if ans==None:
            ans=s[i]&s[i-1]
        else:
            ans=ans&s[i]&s[i-1]
    print(ans)
