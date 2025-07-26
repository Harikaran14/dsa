t = int(input())
for _ in range(t):
    b1,l1,b2,l2,b3,l3=map(int,input().split())
    ans=0
    if l1==l2 and l2==l3 and b1+b2+b3==l1:
        ans=1
    if l1==l2:
        if b1+b2==b3 and l1+l3==b3:
            ans=1
    if l1==l3:
        if b1+b3==b2 and l1+l2==b2:
            ans=1   
    if l3==l2:
        if b3+b2==b1 and l1+l3==b1:
            ans=1
    if l1 +l2==l3 and b1==b2 and b1 +b3==l3:
        ans=1
    if l1 +l3==l2 and b1==b3 and b1 +b2==l2:
        ans=1
    if l3 +l2==l1 and b3==b2 and b1 +b3==l1:
        ans=1        

    if b1==b2 and b2==b3 and l1+l2+l3==b1:
        ans=1
    if ans:
        print("YES")
    else:
        print("NO")                           
    