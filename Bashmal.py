t=int(input())
for _ in range(t):
    n=int(input())
    x=list(input().split())
    s=x[0]
    for i in x[1:]:
        for j in range(min(len(s),len(i))):
            if s[j]>i[j]:
                s=i+s
                break
            if s[j]<i[j]:
                s+=i
                break

            if j==min(len(s),len(i))-1:
                t=j
                if len(s)>len(i):
                    while t<len(s) and  s[t]==i[j]:
                        t+=1
                    if t<len(s) and s[t]<i[j]:
                        s=s+i
                    else:
                        s=i+s
                else:
                    while t<len(i) and  i[t]==s[j]:
                        t+=1
                    if t<len(i) and i[t]<s[j]:
                        s=i+s
                    else:
                        s=s+i
    print(s)


