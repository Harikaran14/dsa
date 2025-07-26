t = int(input())  
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()) )

    for i in range(n-1):
        while True:
            while a[i+1]%a[i]==0:
                if a[i]==1:
                    a[i]+=1
                elif a[i+1]>a[i]:
                    a[i+1]+=1
                else:
                    a[i]+=1
            
            if i>0 and a[i]%a[i-1]==0:
                while a[i]%a[i-1]==0:
                    if a[i]==1:
                        a[i]+=1
                    elif a[i-1]>a[i]:
                        a[i-1]+=1
                    else:
                        a[i]+=1

            if a[i+1]%a[i]!=0:
                break  

    for i in a:
        print(i,end=' ')
    print()                    
                


