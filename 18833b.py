t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    a=0
    for i in d.keys():
        if d[i]%2!=0:
            a+=1
    if a>k+1:
        print("NO")
    else:
        print("YES")
