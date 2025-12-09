t=int(input())
for _ in range(t):
    n=int(input())
    s=[]
    for i in range(n):
       x=list(map(int,input().split()))
       x.append(i)
       s.append(x)
    s.sort(key= lambda x: (-x[0],-x[1]))
    b=[]
    ans=0
    while len(s)!=0:
        x=set()
        mini=float("inf")
        maxi=-float("inf")
        temp=[]
        c=[]
        for i in range(len(s)-1,-1,-1):
            if s[i][1] not in x or s[i][0] not in x:
                if i==len(s)-1:
                    curleft=s[i][0]
                    curright=s[i][1]
                    if i==0:
                        c.append((curleft,curright))
                else:
                    if s[i][0]<=curright:
                        curright=max(curright,s[i][1])
                        if i==0:
                            c.append((curleft,curright))
                    else:
                        c.append((curleft,curright))
                        curleft=s[i][0]
                        curright=s[i][1]

                
                
                x.add(s[i][0])
                x.add(s[i][1])
                temp.append(s[i][2]+1)
                s.pop(i)
        tempans=0
   
        for i in c:
            tempans+=i[1]-i[0]
        if tempans>ans :
            ans=tempans
            b=temp[::]


        
    print(len(b))
    print(*b)

            