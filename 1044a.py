t=int(input())
for _ in range(t):
    k=int(input())
    l=list(map(int,input().split()))
    x=set()
    ans="NO"
    for i in l:
        if i in x:
            ans="YES"
            break
        x.add(i)
    print(ans)