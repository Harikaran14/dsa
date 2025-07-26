'''t=int(input())
for _ in range(t):
    n=input()
    
    while len(n)>1:
        x=0
        for i in n:
            x+=int(i)
        n=str(x)
    print(x)        

t=int(input())
for _ in range(t):
    n=int(input())
    op=0
    for i in range(1,n):
        op+=i
    print(op)  
    
'''
def ass2():
    n=int(input())
    a=[0]*n
    x=0
    a[0]=1
    for i in range(1,n):
        x+=i
        x=x%n
        a[x]=1    
    if 0 in a:
        print("NO")
    else:
        print("YES")     
