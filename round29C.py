import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    segments = s.split("11")
    if n==2:
        print("YES")
        return
    for seg in segments[1:len(segments)-1]:
        if not seg:
            continue

        if "00" in seg:
            continue
        

        if seg.count('0') % 2 == 1:
            print("NO")
            return
    if segments[0]:
        if s[0]=='0':
            pass
        else:
            if "00" in segments[0]:
                pass
        

            elif segments[0].count('0') % 2 == 1:
                print("NO")
                return
    if segments[len(segments)-1]:
        if s[n-1]=='0':
            pass
        else:
            if "00" in segments[len(segments)-1]:
                pass
        

            elif segments[len(segments)-1].count('0') % 2 == 1:
                print("NO")
                return
    print("YES")


t = int(sys.stdin.readline())
for _ in range(t):
    solve()






