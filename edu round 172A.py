t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    x.sort(reverse=True)
    a=0
    for i in x:
        a+=i
        if a>k:
            a-=i
            print(k-a)
            a+=i
            break
        elif a==k:
            print(k-a)
            break
    if a<k:
        print(k-a)    

        

            
