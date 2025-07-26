'''t=int(input())
for i in range(t):
    inp=input()
    spl=inp.split()
    n=int(spl[0])
    k=int(spl[1])
    max1=0
    for i in range(n):
        
        if k**i>n:
            break
        else:
            max1=i
    total=0
    for j in range(max1,-1,-1):
        if n==0:
            break
        quot=n//(k**j)
        if quot >0:
            total+=quot 
            n=n%(k**j)
    print(total)'''

t=int(input())
for _ in range(t):
    k=int(input())
    l=[1,1]
    while True:
        for i in range(1,len(l)+1):
            for j in range(1,len(l)+1):
                if j%i==0:
                    l[j-1]=abs(l[j-1]-1)
        if sum(l)==k:
            print(len(l))
            break

        else:
            l=[1 for i in range(len(l)+1)]
            
           
        
        