n=int(input())
s=input()
c=s.count('+')

q=int(input())
for i in range(q):
    a,b=map(int, input().split())
    if a==b:
        if c==n-c:
            print("YES")
        else:
            print("NO")
    else:
        if ( a*(n-2*c)%(a-b)==0 or a*(n-2*c)%(a-b)==0 )and (c-n<= b*(n-2*c)//(a-b)<=c or c-n<=a*(n-2*c)//(b-a)<=c):
            print("YES")
        else:
            print("NO")