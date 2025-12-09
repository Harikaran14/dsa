t=int(input())
for _ in range(t):
    n=int(input())
    y=[]
    s=[0]*(2*10**5+2)
    for i in range(n):
        a=list(map(int,input().split()))
        for i in range(1,a[0]+1):
           s[a[i]]+=1
        y.append(a)

    ans=False
    for i in y:
        for j in range(1,i[0]+1):
          if s[i[j]]-1>=1:
            ans=True
          else:
            ans=False
            break
          
          
        if ans:
           break

    if ans:
       print("YES")
    else:
       print("NO")
        
           
