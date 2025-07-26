t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    x=a
    y=b
    z=c
    while x<=b and y<=c and z<=d:
        if x>y+z:
            if y>z+x:
                if z>x+y:
                    print(f'{x} {y} {z}')
                    break
                else:
                    z+=1
            else:
                y+=1
        else:
            x+=1