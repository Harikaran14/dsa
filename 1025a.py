t = int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    x=0
    for i in range(1,n):

        if a[i]==a[i-1] and a[i]==0:
            print("YES")
            break
        if a[i]==1:
            x+=1
       
        if i==n-1:
            if x==n-1 and a[0]==1:
                print("YES")
            else:
                print("NO")
            