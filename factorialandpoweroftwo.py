x=[]
v=6
s=4
end=10**12+5
while v<=end:
    x.append(v)
    v*=s
    s+=1
e=len(x)
t = int(input())
for _ in range(t):
    n=int(input())
    ans=[100]
    def rec(ind,val,takes):
        global ans
        if val>n:
            return
        if ind==e:
            v=n-val
            new=takes
            while v:
                v&=v-1
                new+=1
            ans[0]=min(ans[0],new)
            return
        rec(ind+1,val+x[ind],takes+1)
        rec(ind+1,val,takes)
    rec(0,0,0)
    print(ans[0])

