t=int(input())
for _ in range(t):
    n=int(input())
    y,r=map(int,input().split())
    a=min(n,r+y//2)
    print(a)