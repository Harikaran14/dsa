from math import gcd
l=[]
for i in range(1,1001):
    for j in range(i,1001):
        if gcd(i,j)==1:
            l.append([i,j])

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=-1
    x={}
    for i in range(len(a)):
        x[a[i]]=i+1
    s=set(a)
    for i in l:
        if i[0] in s and i[1] in s:
            ans=max(ans,x[i[0]]+x[i[1]])
    print(ans)