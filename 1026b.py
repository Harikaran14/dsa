t = int(input())
for _ in range(t):
    s=input()
    if s.count('(')!=s.count(')'):
        print("NO")    
    elif ")(" in s:
        x=''
        bal=0
        maxi=0
        for i in s:
            if i=='(':
                bal+=1
                x+=str(bal)
            else:
                bal-=1
                x+=str(bal)
            maxi=max(bal,maxi)
        if "()()" in s:
            if "1010" in x:
                print("YES")
            elif  maxi>1:
                b=f"{maxi}{maxi-1}{maxi}"
                if b in x or x=='':
                    print("NO")   
                else:
                    print("YES")
            else:
                print("YES")
        else:
            print("YES")
               
    else:
        print("NO")

