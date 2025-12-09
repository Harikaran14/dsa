t=int(input())
for i in range(t):
    n,q= map(int, input().split())
    s=list(map(str,input()))
    a=list(map(int, input().split()))
    
    for i in a:
        if 'B' not in s:
            print(i)
        else:
            ans=0
            t=i
            while t>0:
                for j in s:
                    if t<=0:
                        break
                    if j=='B':
                        t=t//2
                    else:
                        t-=1
                    ans+=1
            print(ans)

    