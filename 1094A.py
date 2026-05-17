t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ea=[]
    oa=[]
    eb=[]
    ob=[]
    for i in range(n):
        if i%2==0:
            ea.append(a[i])
        else:
            oa.append(a[i])
    
    for i in range(k):
        if b[i]%2==0:
            ob.append(b[i])
        else:
            eb.append(b[i])
    
    ea.sort(reverse=True)
    oa.sort(reverse=True)
    ans=sum(a)

    l=0
    for i in range(len(eb)):
        if l>=len(ea):
            break
        if ea[l]>0:
            ans-=ea[l]
        else:
            if l==0:
                ans-=ea[l]
        l+=1
    l=0

    for i in range(len(ob)):
        if l>=len(oa):
            break
        if oa[l]>0:
            ans-=oa[l]
        else:
            if l==0:
                ans-=oa[l]
        l+=1
    print(ans)