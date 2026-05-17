
t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    three=0
    two=0
    ans=True
    temp=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            if temp>3:
                ans=False
                break
            temp+=1
            if temp==2:
                two+=1
            if temp==3:
                three+=1
                two-=1
        else:
            temp=1
    if three>1:
        ans=False
    if two>2:
        ans=False
    print(three,two)
    if three and two:
        ans=False
    if ans:
        print("YES")
    else:
        print("NO")
            