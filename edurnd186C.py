t=int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans=0

    for i in range(n):
        for j in range(n):
            if a[j]>=b[(j+i)%n]:
                break
            if j==n-1:
                ans+=1
    fin=0
    for i in range(n):
        for j in range(n):
            if b[j]>=c[(j+i)%n]:
                break
            if j==n-1:
                fin+=1
    print(fin*ans*n)

            