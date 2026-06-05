t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    d={}
    for i in range(26):
        x=chr(ord('a')+i)
        d[x]=0
    
    for i in s:
        d[i]+=1
    if n==1:
        print(s)
        continue
    ans=float('inf')
    y=-1
    e=list(d.items())
    e.sort(key=lambda x:-x[1])
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            keep=0
            for j in range(n//i):
                keep+=min(e[j][1],i)
            if n-keep<ans:
                ans=n-keep
                val=i

            if (n//i)!=i:
                keep=0
                for j in range(n//(n//i)):
                    keep+=min(e[j][1],n//i)
                if n-keep<ans:
                    ans=n-keep
                    val=n//i
    
    r=n//val-1
    fin=[]
    use=set()
    l=0
    for i in range(n//val):
        use.add(e[i][0])
    for i in s:
        if i not in use:
            if d[e[r][0]]<val:
                d[e[r][0]]+=1
                fin.append(e[r][0])
            else:
                r-=1
                d[e[r][0]]+=1
                fin.append(e[r][0])
        else:
            fin.append(i)
    for i in range(n):
        if d[fin[i]]>val:
            \
            d[fin[i]]-=1
            if d[e[r][0]]<val:
                d[e[r][0]]+=1
                fin[i]=e[r][0]
            else:
                r-=1
                d[e[r][0]]+=1
                fin[i]=e[r][0]
  
    print(ans)
    print(''.join(fin))



