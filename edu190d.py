t=int(input())
for _ in range(t):
    n = int(input())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    ta=0
    tb=0
    x=[0]*n
    for i in range(n):
        if a[i]==ta+1 and b[i]==tb+1 and a[i]==b[i]:
            x[i]=1
        elif a[i]!=ta+1 and b[i]!=tb+1 and b[i]!=tb and a[i]!=ta:
            x[i]=1 
        if a[i]==ta+1:
            ta+=1
        if b[i]==tb+1:
            tb+=1
        
    ans=[]
    temp=0
    for i in x:
        if i==1:
            temp+=1
        else:
            ans.append(temp)
            temp=0
    if temp:
        ans.append(temp)
    print(x)
    val=0
    for i in ans:
        val+= i*(i+1)//2
    if 0 in x and 1 in x:
        val+=1
    print(val)
