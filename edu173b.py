t = int(input())  

for _ in range(t):
    n, d = map(int, input().split())  
    odd_digits = [1, 3, 5, 7, 9]  
    result = []

    for x in odd_digits:
        if d % x == 0:  
            result.append(x)
    if n>=3 and 3 not in result:
        result.append(3)
    if n>=3 and 7 not in result:
        result.append(7)    
    if n>=6 and 9 not in result:
        result.append(9)  
    if( d==6 or  d==3)and n>=3 and 9 not in result:
        result.append(9)

    result.sort()
    print(" ".join(map(str, result)))