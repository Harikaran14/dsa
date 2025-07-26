t = int(input())
for _ in range(t):
    x, m = map(int, input().split())
    tt = 0
    s=[]
    for i in range(1, m+1):

        op = x ^ i

        
        if op % x == 0 or op % i == 0:
            tt += 1
            s.append(i)
    print(s)
    print(tt)
