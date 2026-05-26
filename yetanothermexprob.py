t=int(input())
for _ in range(t):
    n,k =map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    x=set()
    e=0
    for i in a:
        if i not in x and e<k-1:
            x.add(i)
            e+=1
    for i in range(max(x)+2):
        if i not in x:
            print(i)
            break
    