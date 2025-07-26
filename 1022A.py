t=int(input())
for _ in range(t):
    n=int(input())
    maxi=0
    for i in range(1,n+1):
        maxi+=abs(i-n+i)
    print(maxi//2 +1)    

    