t=int(input())
for _ in range(t):
    n=int(input())
    x=input()
    s=[]
    for i in x:
        s.append(int(i))

    for i in range(n-2):
        if s[i]==s[i+2] and s[i]==1:
            s[i+1]=1
    a2=s.count(1)

    for i in range(n-2):
        if s[i]==s[i+2] and s[i]==1:
            s[i+1]=0
    a1=s.count(1)
    print(a1,a2)
