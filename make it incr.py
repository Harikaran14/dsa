t = int(input())  
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()) )
    a.reverse()
    ans=0
    for i in range(n-1):
        if a[i]==0:
            ans=-1
            break
        while a[i]<=a[i+1] and a[i+1]>0:
            a[i+1]=a[i+1]//2
            ans+=1

    print(ans)
    

            


