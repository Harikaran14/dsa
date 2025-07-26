
t = int(input())
for _ in range(t):
    n,c=map(int,input().split())
    
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]+=i+1
    a.sort()
    s=a[0]
    l=0
    while s<=c and l<n:
        l+=1
        if l<n:
            s+=a[l]
        
        
    print(l)






       