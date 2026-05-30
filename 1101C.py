t=int(input())
for _ in range(t):
    n,x,s=map(int,input().split())
    a=input()
    aori=0
    aa=0
    limit=0
    e=0
    ans=0
    for i in a:
        if i=="I":
            if aori<x:
                aori+=1
                limit+=s-1
                ans+=1
            else:
                if aa>0 and e+1<=limit-(s-1):
                    aa-=1
                    ans+=1
                    e+=1

        if i=="A":
            if aori<x:
                aa+=1
                aori+=1
                limit+=s-1
                ans+=1
            else:
                if e+1<=limit:
                    e+=1
                    ans+=1
        if i=="E" and e+1<=limit:
            e+=1
            ans+=1
    print(ans)