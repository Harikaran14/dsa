t = int(input())  

for _ in range(t):
    n, q = map(int, input().split())  
    a=list(map(int, input().split()) )
    s=0
    b=[]
    b.append(0)
    for i in a:
        s+=i
        b.append(s)
    for i in range(q):
        l,r,k=map(int, input().split()) 
        if (b[l-1] + (r-l+1)*k + b[n]-b[r])%2==0:
            print("NO")
        else:
            print("YES")    