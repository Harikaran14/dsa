t = int(input())
for _ in range(t):
    n,s= map(int, input().split())
    x=list(map(int, input().split()))

    maxi=max(x)
    mini=min(x)
    if s>=maxi:
        print(s-mini)    
    elif s<=mini:
            print(maxi-s)
    else:
        if maxi-s>=s-mini:
            print((s-mini)+(maxi-mini))
        else:
             print((maxi-s)+(maxi -mini))


                