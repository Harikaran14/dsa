t = int(input())
for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    a.sort()
    mineven=n
    minodd=n
    maxeven=0
    maxodd=0
    for i in range(n):
        if mineven==n and a[i]%2==0:
            mineven=i
        elif minodd==n and a[i]%2!=0:
            minodd=i
    a.reverse() 
    for i in range(n):
        if maxeven==0 and a[i]%2==0:
            maxeven=i+1    
        elif maxodd==0 and a[i]%2!=0:
            maxodd=i+1         

    print(min(minodd+maxodd-1,mineven+maxeven-1))        