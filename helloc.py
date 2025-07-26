t=int(input())
for _ in range(t):
    n=input()
    x={'2':0,'3':0}
    sm=0
    for i in n:
        sm+=int(i)
        if i=='2':
            x['2']+=1
        elif i=='3':
            x['3']+=1
    y=False
    for i in range(min(9,x['2'])):
        for j in range(min(9,x['3'])):
            if (sm + i*2 +j*6)%9==0:
                y=True
                break
            
        if y==True:
            break
    print("YES" if y else "NO")    
            
            