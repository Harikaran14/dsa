
t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    st=[]
    for i in a:
        if st and st[-1]==i:
            st.pop()
        else:
            st.append

    if len(st)>0:
        print("NO")
    else:
        print("YES")
        
        