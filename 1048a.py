t = int(input())  
for _ in range(t):
    k,x=map(int, input().split())
    fin=2**k
    if x==fin:
        print(0)
        print()
    else:
        a=False
        if x>fin:
            x=2*fin-x
            a=True
        s=[1]
        x*=2
        while x!=fin:
            if x<2*fin-x:
                x*=2
                s.append(1)
            else:
                x-=2*fin-x
                s.append(2)
        print(len(s))
        s.reverse()
        if a:
            l=[]
            for i in s:
                if i==2:
                    l.append(1)
                else:
                    l.append(2)
            print(*l)
        else:
            print(*s)