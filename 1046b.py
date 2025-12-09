t = int(input())  
for _ in range(t):
    n,k=map(int, input().split())
    s=input()
    maxi=0
    temp=0
    for i in s:
        if i=='1':
            temp+=1
            maxi=max(maxi,temp)
        else:
            temp=0

    if maxi>=k:
        print("NO")
    else:
        print("YES")
        x=1
        y=[0]*n
        for i in range(n):
            if s[i]=='1':
                y[i]=str(x)
                x+=1
        for i in range(n):
            if s[i]=='0':
                y[i]=str(x)
                x+=1
        print(*y)

    