t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    ans=0
    binary_string = bin(x)[2:]
    ans+=binary_string.count('1')
    sumi=x
    if x==0:
        if n==1:
            print(-1)
        elif n%2==0:
            print(n)
        elif n%2!=0:
            print(n+3)
    elif x==1:
        if n%2==1:
            print(n)
        else:
            print(n+3)
    else:
        if n<=ans:
            print(sumi)
        else:
            if (n-ans)%2==0:
                print(sumi + n-ans)
            else:
                print(sumi + n-ans+1)  