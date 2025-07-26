t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    adist=[]
    bdist=[]

    for i in range(n):
        if a[i] not in adist:
            adist.append(a[i])
        if len(adist)>=3:
            break
    
    for i in range(n):
        if b[i] not in bdist:
            bdist.append(b[i])
        if len(bdist)>=3:
            break
    print(adist,bdist)
    if len(adist)>=3 or len(bdist)>=3:
        print("YES")
    elif len(adist)>=2 and len(bdist)>=2:
        print("YES")

    else:
        print("NO")        
