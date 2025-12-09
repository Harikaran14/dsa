
t=int(input())
for _ in range(t):
    n=int(input())
    b=[]
    for i in range(n):
        a=list(map(int,input().split()))
        a.append(i+1)
        b.append(a)
    b.sort(key= lambda x :x[0])
    l=set()
    r=set()
    for i in range(n):
        if i<n//2:
            l.add(b[i][2])
        else:
            r.add(b[i][2])
    q1=[]
    q2=[]
    q3=[]
    q4=[]
    b.sort(key= lambda x :x[1])
    for i in range(n):
        if i<n//2:
            if b[i][2] in l:
                q1.append(b[i][2])
            else:
                q2.append(b[i][2])
        else:
            if b[i][2] in l:
                q4.append(b[i][2])
            else:
                q3.append(b[i][2])
  
    for i in range(len(q1)):
        print(q1[i],q3[i])
    for i in range(len(q2)):
        print(q2[i],q4[i])




    

                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                 