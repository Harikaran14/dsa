t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    s=0
    b=[]
    temp=0
    for k,v in d.items():
        
        if v%2!=0:
            s+=max(0,v-1)*k
            b.append(k)
            temp+=v-1
        else:
            s+=v*k
            temp+=v
    b.sort(reverse=True)
    if s!=0:
        if temp<2:
            s=0
    
        else:
            l=0
            while l<len(b):
                if b[l]<s:
                    s+=b[l]
                    l+=1
                    break
                l+=1
            
            if l<len(b) and l+1<len(b) and b[l]<s-b[l]+b[l+1]:
                s+=b[l+1]
    print(s)