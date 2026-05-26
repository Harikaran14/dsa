t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k%2!=0:
        
        ans=[n]*(k)
        print(*ans)
    else:
        ans=[n]*(k-2)
        if n&(n-1)==0:
            ans.append(0)
            ans.append(n)

        else:
            
            x=bin(n)[3:]
           
            l=len(x)
            s=1
            maxi=n
            v=n
            while l>=0 :
                if x[l]=='0':
                    ansinbin='0'+ x[:l]+'1'+x[l+1:]
                    x='0'+ x[:l]+'1'+x[l+1:]
                    print(ansinbin)
                    aint=int(ansinbin,2)
                    print(aint)
                    if aint <= n and n^aint<=n and aint+n^aint>maxi :
                        maxi=max(aint+n^aint,maxi)
                        v=aint
                        
                       
                l-=1
                s+=1
                
            
            ans.append(v)
            ans.append(v^n)
        print(*ans)