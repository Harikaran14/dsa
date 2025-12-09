import sys
input = sys.stdin.readline

t=int(input())


for _ in range(t):
    n,k=map(int,input().split())
    aa=list(map(int,input().split()))
    aa.sort()
    a=set(aa)
    b=set()
    ans=True
    if 1 in a:
        b.add(1)
        if len(a)!=k:
            ans=False
    else:
        b=a.copy()
        for i in sorted(list(a)):
            if k//i>n:
                ans=False
                break
            if i not in b:
                continue
            for j in range(i,k+1,i):
                if i==j:
                    continue
                if j not in a:
                    ans=False 
                    break
                if j in b:
                    b.remove(j)
            
            if ans==False:
                break
    if ans:
        print(len(b))
        print(*list(b))
    else:
        print(-1)