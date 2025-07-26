t = int(input())
for _ in range(t):
    n,c= map(int, input().split())
    s=list(map(int, input().split()))
    a=4*n
    b=0
    k=0
    for i in s:
        b+=i
        k+=i*i
    k-=c    
    b*=4

    ans1=(-b + (b**2 -4*a*k)**0.5)//(2*a)
    ans2=(-b - (b**2 -4*a*k)**0.5)//(2*a)
    if  ans1 >=0 and ans2>=0:
        print(int(min(ans1,ans2)))
    else:
        print(int(max(ans1,ans2)))    


        