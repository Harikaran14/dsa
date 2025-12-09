t=int(input())
for _ in range(t):
    n=int(input())
    odd=[]
    even=[]
    re=[]
    ro=[]
    for i in range(n,0,-1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    for i in range(1,n+1):
        if i%2==0:
            re.append(i)
        else:
            ro.append(i)
    ans=even + [odd[0]]+re 
    if n%2==0:
        ans+=odd[1:len(odd)-1]+[odd[0]]+ro[:len(ro)-1]+[1]
    else:
        ans+=odd[1:]+[odd[0]]+ro[1:len(ro)-1]+[1]
    if n<=2:
        ans.pop()
    print(*ans)