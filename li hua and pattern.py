t = int(input())
for _ in range(t):
    n, k= map(int, input().split())
    x=[]
    for i in range(n):
        a=list(map(int, input().split()))
        x.append(a)
    ans=0
    for i in range((n+1)//2):
        for j in range(n):
            if x[i][j]!=x[n-i-1][n-j-1] :
                if i<n-i-1 or (i==n-i-1 and n-j-1>j): 
                    ans+=1    
    print(ans)                
    if n==1 or ans==k or ( ans<k and ((k-ans)%2==0 or n%2!=0)):
        print("YES")
    else:
        print("NO")          
