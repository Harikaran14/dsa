t = int(input())  
for _ in range(t):
    n, k = map(int, input().split())  
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    l=0
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i]==0:
            a[i]=b[l]
            l+=1
    x=True
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            x=False
            break
    if x:
        print("NO")
    else:
        print("YES")
    
            