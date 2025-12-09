
import sys

t=int(input())
for _ in range(t):
    n=int(input())
    bn=bin(n)[2:]
    take=[i for i in range(1,n)]

    t=0
    y=[i for i in range(1,n+1)]
    for i in y:
        if i & 1!=0:
            t+=1
            
    for x in range(len(bn)):
        s=0
        a0=[]
        a1=[]
        t0=[]
        t1=[]
        for i in take:
            print(f"? {i} {2**x}")
            sys.stdout.flush()
            b=int(input())
            if b==0:
                t0.append(i)
            else:
                t1.append(i)
                s+=1
        for i in y:
            if i & int(2**(x))!=0:
                a1.append(i)
            else:
                a0.append(i)
     #   print(a0,a1,t0,t1,s,t)
        if t==s:
            take=t0
            y=a0
            t=0
            for i in y:
                if i & int(2**(x+1))!=0:
                    t+=1
        else:
            take=t1
            y=a1
            t=0
            for i in y:
                if i & int(2**(x+1))!=0:
                    t+=1
      #  print(take)
     #   print(y)
    print(f"! {y[0]}")
 

