mod=676767677
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    right=n
    left=0
    fin=0
    while left<=right:
        mid=(left+right)//2
        x=[0]*n
        y=[]
        for i in a:
            if i<n and x[i]!=-1 and i<mid:
                x[i]=-1
            else:
                y.append(i)

        m=len(y)
        l=0
        for i in range(n):
            if x[i]!=-1:
                while l<m and y[l]%(y[l]//2 +1)<i:
                    l+=1
                if l==m:
                    break
                else:
                    x[i]=-1
                    l+=1
        ans=n
        for i in range(n):
            if x[i]!=-1:
                ans=i
                break
        if ans>=mid:
            fin=ans
            left=mid+1
        else:
            right=mid-1
    print(fin)    

            


