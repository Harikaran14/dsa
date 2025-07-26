t=int(input())
for _ in range(t):
    n=int(input())
    total=1
    while n>3:
        n=n//4
        total*=2
    print(total)     
