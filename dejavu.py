
x=1
y=[1]
while x<=30:
    y.append(y[x-1]*2)
    x+=1    

t = int(input())
for _ in range(t):
    n,q= map(int, input().split())
    a=list(map(int, input().split()))
    x=list(map(int, input().split()))
    m=float('inf')
    mini=min(x)
    for i in x:
        if i<m:
            m=i
            for j in range(n):
                if a[j]% y[i]==0:
                    a[j]+=y[i-1] 
            if m==mini:
                break
                                       
    for i in a:
        print(i,end=' ')
    print() 
















'''    
    x.sort(reverse=True)
    d={}
    for i in a:
        d[i]=[]
    s=[0]    
    p=[]
    for i in range(q-1,-1,-1):
        ap=2**(x[i]-1)
  
        s.append(s[q-1-i]+ap)
        p.append(ap)
    s.reverse()
    p.reverse()
    print(s,p)
    new=[]
    for j in a:
        for i in range(len(p)):
            if j%(p[i]*2)==0:
                new.append(j+s[i])
                break
            elif i==q-1:
                new.append(j)
    for i in new:
        print(i,end=' ')
    print() '''