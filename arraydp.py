t = int(input())  
for _ in range(t):
    n = int(input()) 
    c=list(map(int, input().split()) )
    x=c[::]
    x.sort()
    p=[]
    s=0
    for i in x:
        s+=i
        p.append(s)
    l=1
    r=0
    d={}
    temp=0
   
    while r<n and l<n:
        if x[l]<=p[r]:
            l+=1
            r+=1
        else:
            while temp<=r:
                d[x[temp]]=l-1
                temp+=1
            l+=1
            r+=1    
            
    if list(d.values()).count(0)>1:
        print(f"{n-1} "*n)
    else:
        for i in c:
            if i in d.keys():
                print(d[i], end=' ')
            else:
                print(n-1 , end=' ')
        print()   
