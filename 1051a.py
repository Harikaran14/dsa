t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in range(n):
        d[a[i]]=i+1
    last=d[n]
    ans=True
    left=0
    right=0
    for i in range(n-1,0,-1):
        if d[i]==max(1,last-left-1):
            left+=1
        elif d[i]==min(n,last+right+1): 
            right+=1
        else:
            ans=False
            break
    if ans:
        print("YES")
    else:
        print("NO")
