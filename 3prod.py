t=int(input())
for _ in range(t):
    n=int(input())
    tn=n
    x=[]
    temp=set()
    v=1
    for i in range(2,int(n**0.5)+1):
        while n%i==0:
            temp.add(i)
            x.append(i)
            v*=i
            n=n//i
    if tn//v!=1:
        temp.add(tn//v)
        x.append(tn//v)
    temp=list(temp)
    print(x)
    if len(temp)==0:
        print("NO")
    elif len(temp)==1:
        if len(x)>=6:
            third=1
            for i in range(3,len(x)):
                third*=x[i]
            print("YES")
            print(x[0],x[1]*x[2],third)
        else:
            print("NO")
    elif len(temp)==2:
        if len(x)>3:
            print("YES")
            third=1
            for i in range(len(x)):
                third*=x[i]
            print(temp[0],temp[1],int(third/temp[0]/temp[1]))
        else:
            print("NO")
    else:
        third=1
        for i in range(len(x)):
            third*=x[i]
        print("YES")
        print(temp[0],temp[1],int(third/temp[0]/temp[1]))
    