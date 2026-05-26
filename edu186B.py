t=int(input())
for _ in range(t):
    a,b = map(int, input().split())  
    c,d=a,b
    layer=0
    s=1
    turn=1
    while True:
        if turn:
            if a<s:
                break
            a-=s
        else:
            if b<s:
                break
            b-=s
        
        layer+=1
        s*=2
        turn=not turn 

    l=0
    s=1
    turn=0
    a,b=c,d
    while True:
        if turn:
            if a<s:
                break
            a-=s
        else:
            if b<s:
                break
            b-=s
        
        l+=1
        s*=2
        turn=not turn 
    print(max(l,layer))
'''
        

    mini=min(a,b)

    x=1
    c=1
    y=1
    while x<=mini:
        c=c*4
        x+=c
        y+=2
    x-=c
    c=c/4
    y-=2
    temp=True
    print(x,c,y)
    if x*2 <= mini:
        y+=1
        c=c*2
        x+=c
        temp=False
    
    print(x,c,y)

    if not temp and max(a,b)>=x-c + c*2:
        y+=1
    if  temp and max(a,b)>=(x-c)*2:
        y+=1
    print(y)
    

    '''