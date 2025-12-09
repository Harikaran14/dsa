t = int(input())  
for _ in range(t):
    a,b,c,d=map(int, input().split())
    c=c-a
    d=d-b
    if (min(a,b)+1)*2>=max(a,b) and (min(c,d)+1)*2>=max(c,d):
        print("YES")
    else:
        print("NO")