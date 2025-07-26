t = int(input())
for _ in range(t):
    n, m,p,q = map(int, input().split())
    if n%p!=0:
        print("YES")
    else:
        if (n//p)*q==m:
            print("YES")
        else:
            print("NO")        