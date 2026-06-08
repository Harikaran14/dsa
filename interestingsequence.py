t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    temp=0
    nbin=bin(n)[2:].zfill(100)
    xbin=bin(x)[2:].zfill(100)
    ans=True
    fin=-1
    xbin=xbin[::-1]
    nbin=nbin[::-1]
    if x>n:
        print(-1)
        continue
    if x==n:
        print(n)
        continue
    for i in range(len(nbin)):
        if nbin[i]=='1' and xbin[i]=='0':
            temp=1
            fin=i
        if nbin[i]=='0' and xbin[i]=='1':
            ans=False
            break   
        if nbin[i]=='0' and xbin[i]=='0':
            if temp:
                fin=i
                temp=0
        if nbin[i]=='1' and xbin[i]=='1' and temp>0:
            ans=False
            break
    if not ans:
        print(-1)
    else:
        ans='0'*(fin)+'1'+nbin[fin+1:]
        
        print(int(ans[::-1],2))
