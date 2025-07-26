'''t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    s=input()
    for j in range(100):
        for i in s:
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1
            elif i == "W":
                x -= 1
            l.append([x, y])
            
    if [a,b] in l:
        print("YES")
    else:
        print("NO")'''

n=int(input())
x=list(map(int, input().split()))
d={1:0,2:0,3:0,4:0}
op=0
for i in x:
    d[i]+=1

if d[2]%2!=0:
        d[1]=d[1]-2
        d[2]=d[2]-1
        op+=1

if d[1]>d[3]:
    

    op+=d[3]+ ((d[1]-d[3]-1)//4)+1 
else:
    op+= d[3]

op+= ((d[2]+1)//2) + d[4]
print(op)
