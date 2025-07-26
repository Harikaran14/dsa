t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    kx,ky=map(int,input().split())
    qx,qy=map(int,input().split())
    l=[0,a+b,a+a,b+b]
    count=0
    for i in l:
        if kx+i==qx or kx-i==qx:
            for j in l:
                if ky + j==qy or ky-j==qy:
                    count+=1
    print(count)            
            