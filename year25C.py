t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    t=[]
    s.append(float("inf"))
    t.append(float("inf"))
    for j in range(n):
        slast=s[len(s)-1]
        tlast=t[len(t)-1]
        if slast>tlast:
            s,t=t,s
        slast=s[len(s)-1]
        tlast=t[len(t)-1]
        if a[j]<= slast:
            s.append(a[j])
        elif a[j]<=tlast:
            t.append(a[j])
        else:
            s.append(a[j])

    op=0
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            op+=1

    for i in range(len(t)-1):
        if t[i]<t[i+1]:
            op+=1 
    print(op)                  