'''
x=input()
y=input()
z=x.split(" ")
a=y.split(" ")
b=[]
c=[]
for i in z:
    b.append(int(i))
for i in a:
    c.append(int(i))
d=b[1]
e=c[d-1]
f=0
for i in c:
    if i>0 and i>=e:
        f+=1
print(f)
'''
for i in range(10,1,-1):
    print(i)
'''
a=int(input())
c=0
for i in range(a):
    x=input()
    if x.startswith( "++" ) or x.endswith( "++" ):
        c+=1
    elif x.startswith( "--" ) or x.endswith( "--" ):
        c-=1
print(c)        
    '''
