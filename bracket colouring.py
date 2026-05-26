t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    x=0
    ans=[]
    for i in s:
        if i=='(':
            x+=1
        else:
            x-=1
    if x!=0:
        print(-1)
    else:
        x=0
        for i in s:
            if i=='(':
                x+=1
            else:
                x-=1
            if x<0:
                ans.append(2)
                x=0
            else:
                ans.append(1)
                
        c2=ans.count(2)

        for i in range(n-1,-1,-1):
            if c2>0 and ans[i]==1 and s[i]=="(":
                ans[i]=2
                c2-=1
        c2=ans.count(2)
        if n==c2:
            for i in range(n):
                ans[i]=1
        y=[]
        x=0
        for i in s:
            if i==')':
                x+=1
            else:
                x-=1
            if x<0:
                y.append(2)
                x=0
            else:
                y.append(1)
        if y.count(1)==n:
            print(1)
            print(*y)
        else:
            print(1 if ans.count(1)==n else 2)
            print(*ans)