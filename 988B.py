t=int(input())
for _ in range(t):
    k=int(input())-2
    l=list(map(int,input().split()))
    x=[0]*(max(l)+1)
    for i in l:
        x[i]+=1
    for i in range(len(x)):
        if x[i]!=0:
            if i*i==k and x[i]>1:
                print(f'{i} {i}')
                break
            elif k%i==0 and x[k//i]>0:
                print(f'{i} {k//i}')
                break
            
             