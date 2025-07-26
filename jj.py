from math import ceil,floor
t = int(input())
for _ in range(t):
    s=input()
    k=0
    t=0
    for i in range(len(s)):
        if s[i]=='1':
            t+=1
            if i==len(s)-1 and s[0]=='1':
                t+=1
            k=max(k,t)
            
        else:
            t=0
    if '1' not in s:
        print(0)
    elif '0' not in s:
        print(n*n)
    else:
        print(floor((k+1)/2)+ceil((k+1)/2))
            