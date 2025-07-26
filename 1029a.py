t=int(input())
for _ in range(t):
    x=int(input())
    l=[0,0,0]
    c=0
    while max(l)<x:
        l.sort()
        l[0]=l[1]*2+1
        c+=1
    c+=2    
    print(c)    




    
