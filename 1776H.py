t=int(input())
for _ in range(t):
    n=int(input())
    t1=list(map(int , input().split()))
    t2=list(map(int , input().split()))
    
    op=0
    if t1==t2:
        print(op)
        continue
    for i in range(n):
        t1.remove(t2.pop(0))
        if t1==t2:
            op=i+1
            break

    print(op)
    