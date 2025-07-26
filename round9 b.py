t=int(input())
for _ in range(t):
    s=input()
    a=None
    for i in range(len(s)-2):
        x=s[i:i+3]
        if x[0]!=x[1] and x[0]!=x[2] and x[1]!=x[2] :
            print(x)
            a=1
            break

        elif x[0]==x[1] :
            print(x[:2])
            a=1
            break
        elif  x[1]==x[2]:
            print(x[1:3])
            a=1
            break
    if len(s)==2 and s[0]==s[1]:
        print(s)
        a=1
        
    if a==None:
        print(-1)    


    