t=int(input())
for _ in range(t):
    l,a,b=map(int,input().split())
    maxi=-float('inf')
    for i in range(5001):
        maxi=max(maxi, (a+i*b)%l)
    print(maxi)
        