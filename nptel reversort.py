x=eval(input())
c=0
n=len(x)
for i in range(n-1):
    elementat=x.index(i+1)
    d=list()
    d.extend(x[:i])
    d.extend(reversed(x[i:elementat+1]))
    d.extend(x[elementat+1:])
    c+=elementat-i+1
    x=d[:]
    print(c)
print(x)    
print(c)    


