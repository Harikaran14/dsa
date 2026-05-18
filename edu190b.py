t=int(input())
for _ in range(t):
    s=input()
    ans=s.count('4')
    odd=0
    two=0
    fix=s.count('2')
    removal=s.count('2')
    for i in s:
        if i=='2':
            two+=1
            removal=min(removal,max(0,fix-two+odd))
        if i=='1' or i=='3':
            odd+=1
    ans+=removal
    print(ans)
