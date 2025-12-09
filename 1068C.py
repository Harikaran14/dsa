t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=set()
    c=[]
    for i in a:
        if i not in b:
            c.append(i)
            b.add(i)


    e=len(c)
    val=(10**18 - n)%e
    print(val)
    if val==0:
        print(c[-1])
    else:
        print(c[val-1])

    