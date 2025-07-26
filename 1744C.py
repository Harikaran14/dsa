t=int(input())
for _ in range(t):
    n,c=map(str, input().split())
    n=int(n)
    s=input()
    if c=='g':
        print(0)
        
    else: 
        mini=[]
        for i in range(n):
            small=[]
            if s[i]==c:
                l=i
                r=n-1
                while r>=0:
                    if s[r]=='g':
                        if r>=l:
                            small.append(r-l)
                        else:
                            small.append(n+(r-l))
                    r-=1 

                mini.append(min(small))
        print(max(mini))    
                        