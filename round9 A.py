t=int(input())
for _ in range(t):
    n=int(input())
    x=[2]
    mod=[0]
    for i in range(2,n+1):
        for j in range(x[i-2],101):
            if j%i not in mod and j not in x:
                x.append(j)
                mod.append(j%i)
                break
    s=' '.join(map(str,x))
    print(s)
    