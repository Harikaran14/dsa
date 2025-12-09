t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    rem = list(map(int, input().split()))
    q.sort()
    rem.sort(reverse=True)
    l=0
    r=0
    ans1=0
    while l<n and r<n:
        if (rem[r]+1)*(q[l]+1)<=k+1:
            ans1+=1
            l+=1
        r+=1
    print(ans1)