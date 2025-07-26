from math import gcd

def findPrimeFactors(n):
    primeFactors = []
    if n % 2 == 0:
        primeFactors.append(2)
        while n % 2 == 0:
            n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            primeFactors.append(i)
            while n % i == 0:
                n //= i
        i += 2
    if n > 2:
        primeFactors.append(n)
    return primeFactors

def findShortestSubsequence(dp, a, index, primeFactors):
    n = len(a)
    for j in range(index, n):
        bitmask = 0
        for p in range(len(primeFactors)):
            if a[j] % primeFactors[p] == 0:
                bitmask |= (1 << p)
        new_dp = dp[:]
        for i in range(len(dp)):
            if dp[i] == n + 1:
                continue
            new_dp[bitmask & i] = min(new_dp[bitmask & i], dp[i] + 1)
        dp[:] = new_dp

def printMinimumLength(a):
    mn = len(a) + 1
    for i in range(len(a) - 1):
        primeFactors = findPrimeFactors(a[i])
        k = len(primeFactors)
        dp = [len(a) + 1] * (1 << k)
        full_mask = (1 << k) - 1
        dp[full_mask] = 1
        findShortestSubsequence(dp, a, i + 1, primeFactors)
        mn = min(mn, dp[0])
    return -1 if mn == len(a) + 1 else mn

# Main execution
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # If all elements are equal
    if a.count(a[0]) == n:
        print(0)
        continue
    
    # Count 1s (since GCD of 1 with anything is 1)
    count_one = a.count(1)
    if count_one > 0:
        print(n - count_one)
        continue

    # Compute GCD of all elements
    g = a[0]
    for i in a:
        g = gcd(g, i)

    if g in a:
        print(n - a.count(g))
    else:
        a = [i // g for i in a]
        ans = printMinimumLength(a)
        if ans == -1:
            print(-1)
        else:
            print(n + ans - 2)
