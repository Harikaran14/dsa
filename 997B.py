t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    a={}
    z=[]
    for i in range(n):
        inpo=input()
        l=[]
        for w in inpo:
            l.append(int(w))
        x.append(l)  
        b=l.count(1)
        a[i]=b
        if b not in z:
            z.append(b)       
    z.sort(reverse=True)
    op=[]
    for i in z:
        s=[]
        for j in a.keys():
            if a[j]==i:
                s.append(int(j))       
        s.sort(reverse=True) 
        t=[]  
        for k in range(len(s)-1):
            for l in range(k+1,len(s)):
                if x[s[k]][s[l]]==1:
                    t.append(s[k])
                    t.append(s[l])
        t.sort()            
        for i in s:
            if i not in t:
                op.append(i)
        op+=t                        
    for i in range(n):
        print(op[i]+1,end=' ')
    print()

