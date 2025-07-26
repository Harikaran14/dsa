t = int(input())
for _ in range(t):
    a,b,c,d= map(int, input().split())
    flower=min(b,d)
    g=min(a,c)
    if flower<=g:
        print('Gellyfish')
    else:
        print('Flower')    