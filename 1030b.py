t = int(input())  
for _ in range(t):
    n=int(input()) 
    print(3+ (n-3)*2)
    for i in range(1,n+1):
        if i!=1:
            print(i, 1 ,i)
        if i+1<n:  
            print(i, i+1, n)
  

                