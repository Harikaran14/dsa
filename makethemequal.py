t=int(input())
for _ in range(t):
    n,x=list(map(str,input().split()))
    n=int(n)
    s=input()
    o=True
    e=True
    for i in range(n):
        if s[i]!=x:

            o=False
        else:
            if (n+1)//2<=i:
                e=False
                y=i

        
    if o==False :
        if e:
            print(2)
            print(n-1, n)
        else:
            print(1)
            print(y+1)
        
    else:
        print(0)
        
    