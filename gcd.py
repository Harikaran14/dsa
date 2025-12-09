t=int(input())
for _ in range(t):
   
    n,l,r=list(map(int,input().split()))
    ans=True
    v=[]
    for i in range(1,n+1):
        if l%i==0:
            v.append(l)

        elif r<l+(i-l%i):
            ans=False
            break
        else:
            v.append(l+(i-l%i))
    if ans:
        print("YES")
        print(*v)
    else:
        print("NO")

