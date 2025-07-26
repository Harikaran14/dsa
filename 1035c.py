t = int(input())  
for _ in range(t):
    n,l,r,k= map(int, input().split())
    if n%2!=0:
        print(l)
    else:
        b=bin(l)[2:]
        x='1'+len(b)*'0'
        x=int(x,2)
        if x<=r:
            if k<n/2:
                print(l)
            else:
                print(x)
        else:
            print(-1)