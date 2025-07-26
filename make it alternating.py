n=200000
x=[0]*(n+1)
x[0]=1


t = int(input())
y=0
for _ in range(t):
    s=input()
    a1=0
    a2=1
    temp=1
    v=0
    for i in range(1,len(s)+1):
        if i<len(s) and  s[i-1]==s[i]:
            temp+=1
        else:
            if temp>1:
                v+=1
                a1+=temp-1
                a2= (a2 *   temp ) % 998244353
                temp=1
    temp=a1

    if x[temp]==0:
        for i in range(y+1,temp+1):
            x[i]=((x[i-1]%998244353)*(i%998244353))%998244353
        y=temp
    a2 = (a2 * x[temp]) % 998244353

    print(a1,max(1,a2))
