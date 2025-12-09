t=int(input())
for _ in range(t):
    s=input()
    print(s.count(s[-1]))
    print(len(s)-s.count(s[-1]))