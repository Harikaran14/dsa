def isPrime(n):

    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
def prime_factors(num):
  factors = []
  factor = 2
  while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
  return factors

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=set(a)
    dp=[0]*(max(max(a),n)+1)
    for i in range(1,max(a)+1):
        if i in x:
            dp[i]=1
    for i in range(1,n+1):
        if dp[i]>0:
            for k in range(i,n+1,i):
                if dp[k//i]>0:
                    if dp[k]==0:
                        dp[k]=dp[i]+dp[k//i]
                    else:
                        dp[k]=min(dp[k],dp[i]+dp[k//i])
    ans=[-1]*n
    for i in range(1,n+1):
        if dp[i]==0:
            ans[i-1]=-1
        else:
            ans[i-1]=dp[i]
    print(*ans)
        
    
    '''dp=[0]*(n+1)
    for i in a:
        if isPrime(i) or i==1:
            dp[i]=1
        else:
            f=prime_factors(i)
            for j in f:
                dp[j]=1
    ans=[-1]*n
    if 1 in a:
        ans[0]=1
    for i in range(2,n+1):
        f=prime_factors(i)
        temp=i
        for j in f:
            if dp[j]==0:
                continue'''
        
           
        


        
