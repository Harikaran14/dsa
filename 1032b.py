t = int(input())
for _ in range(t):
    n=int(input())
    s=input()
    x=set()
    x.add(s[0])
    x.add(s[n-1])
    ans=0
    for i in s[1:n-1]:
        if i in x:
            ans=1
            break
        else:
            x.add(i)
    if ans:
        print("YES")
    else:
        print("NO")
            