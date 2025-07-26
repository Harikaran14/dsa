t = int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    l=0
    for i in a:
        if abs(i)<abs(a[0]):
            l+=1
    if n%2==0 and l==n-l:
        print("YES")
    elif l>n-l-1:
        print("NO")
    else:
        print("YES")    
