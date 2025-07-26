n=int(input())
s=input()
ans=0
for i in range(1,n):
    if ord(s[i])<ord(s[i-1]):
        ans=1
        break
print("YES"if ans else "NO")    