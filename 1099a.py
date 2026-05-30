t=int(input())
for _ in range(t):
    n=int(input())
    x=[1]
    s=set()
    i=2
    while i<=2*n:
        if len(x)>=n:
            break
        if i in s:
            i+=1
            continue
        s.add(x[-1]+i)
        x.append(i)
        i+=1
    print(*x)
        