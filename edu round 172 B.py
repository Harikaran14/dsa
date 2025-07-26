t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int, input().split()))
    d={}
    for i in x:
        if i in d:
            d[i]+=1
        else:
            d[i]=1  
    d={k: v for k, v in sorted(d.items(), key=lambda item: item[1])}          
    alice=0
    taken=[]
    sd=0   
    al=[] 
    bob=[]     
    for k,v in d.items():
        if v%2!=0:
            taken.append(k)
            if sd%2==0:
                alice+=1
                d[k]-=1
                if d[k]==0:
                    alice+=1
            else:
                d[k]-=1
                bob.append(k)

            sd+=1

    for k,v in d.items():
        if k not in taken:
            taken.append(k)
            al.append(k)
        elif k in bob and v>0:
            alice+=1  
    alice+= len(al)
    
    print(alice)        





