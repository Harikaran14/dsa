t = int(input())
for _ in range(t):
    a,b= map(int, input().split())
    q=[]
    for i in range(b):
        p= list(map(int, input().split()))
        q.append(p)
    c=2
    m=1
    n=2
    sides=[1,2]
    while c<a:
        m,n=n,m+n
        c+=1
        sides.append(n)
    sides.reverse()   
    print(sides) 
    ans=''
    for i in q:
        j=0
        mini=min(i[0],i[1])
        h=i[2]
        if h-sides[j]>=0 and sides[j]<=mini:
            if max(i[0]-sides[j],i[1]-sides[j])>=sides[1]:
                success=True  
            elif h-sides[j]-sides[j+1]>=0:
                success=True
            else:
                success=False   
        else:
            success=False                     
            
        
        if success:
            ans+='1'
        else:
            ans+='0'
    print(ans)        
            


