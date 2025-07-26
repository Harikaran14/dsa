
t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=[]
    m1=0
    k=set()
    l=set()
    c=0
    cr=[]
    cc=[]
    r=n
    for s in range(n):
        a=list(map(int,input().split()))
        temp=max(a)

        if m1<temp:
            m1=temp
            c=0
            r=s
        
        c+=a.count(m1)
        x.append(a)

    if c==1:
        cc=n
        for j in range(m):
            if x[r][j] ==m1:
                    cc=j
                    break
        
        for i in range(n):
            for j in range(m):
                if i==r or j==cc:
                    x[i][j]-=1
        m1=0
        for i in x:
            temp=max(i)
            if m1<temp:
                m1=temp
        
        print(m1)



    else:    
        y=[]
        for i in range(n):
            temp=[]
            ans=0
            for j in range(m):
                if x[i][j]==m1:
                    temp.append(1)
                    ans+=1
                else:
                    temp.append(0)
            cr.append(ans)        
            y.append(temp)

        for i in range(m):
            temp=0
            for j in range(n):
                if x[j][i]==m1:
                    temp+=1
            cc.append(temp)
        fin=0
        for i in range(n):
            if fin==1:
                break
            for j in range(m): 
                ans=cr[i]+cc[j]
                if x[i][j]==m1:
                    ans-=1
                if ans==c:
                    fin=1
                    break

        if fin:
            print(m1-1)
        else:
            print(m1)            
        
                

                        





                        
                    
                
                    
            