from collections import deque
s=input()
t=int(input())
for _ in range(t):
    if s=="first":
            n,m=map(int,input().split())
            y=[list() for i in range(n+1)]
            for i in range(m):
                a,b=map(int,input().split())
                y[a].append(b)

                y[b].append(a)
            vs=[0]*(n+1)
            vs[1]='r'
            q=deque()
            q.append([1,0])
            while len(q)!=0:
                cur=q.popleft()
                for i in y[cur[0]]:
                    if vs[i]==0:
                        q.append([i,cur[1]+1])
                        if (cur[1]+1)%3==0:
                            vs[i]='r'
                        elif (cur[1]+1)%3==1:
                            vs[i]='g'
                        else:
                            vs[i]='b'
            ans=''
            for i in vs[1:]:
                ans+=i
            print(ans)

    else:
            q=int(input())
            for j in range(q):
                d=int(input())
                c=input()
                if 'b' not in c:
                    for i in range(d):
                        if c[i]=='g':
                            print(i+1)
                            break
                        if i==d-1:
                            print(1)
                elif 'g' not in c:
                    for i in range(d):
                        if c[i]=='r':
                            print(i+1)
                            break
                        if i==d-1:
                            print(1)
                    
                else:
                    for i in range(d):
                        if c[i]=='b':
                            print(i+1)
                            break
                        if i==d-1:
                            print(1)
                
                

