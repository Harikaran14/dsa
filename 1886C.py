res=[]
t=int(input())
for _ in range(t):
    s=input()
    x=int(input())
    n=len(s)
    l=0
    while x-n>0:
        l+=1
        x-=n
        n-=1
  
    y=x
    x=list()
    for i in s:
        x.append(i)
    
    
    stack=[]
    for i in s:
        while l>0 and stack and stack[-1]>i:
            stack.pop()
            l-=1
        stack.append(i)

    res.append(stack[y-1])
print(''.join(res))