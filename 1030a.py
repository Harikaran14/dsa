t = int(input())  
for _ in range(t):
    n, k = map(int, input().split()) 
    if k==0:
         print('0'*n)
    elif k==1:
         print('1'+'0'*(n-k))     
    elif n-k==0:
         print('1'*n)
    elif n-k==1:
         print('1'*k+'0')
    elif n-k>=2:
         print('10'+'0'*(n-k-2)+'1'*(k-2)+'10')
