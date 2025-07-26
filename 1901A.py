t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=[0]
    l+=list(map(int,input().split()))
    x=0
    for i in range(1,len(l)):
        if l[i]-l[i-1]>x:
            x=l[i]-l[i-1]
    edge=((k-l[len(l)-1]) * 2)
    if edge>x:
        x=edge        
    print(x)
    