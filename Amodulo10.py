t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=True
    if a[0]%5==0:
        if a[0]%10==0:
        
            for i in a:
                if i%10==0 :
                    if i!=a[0]:
                        ans=False
                        break
                else:
                    if i+5!=a[0]:
                        ans=False
                        break
        else:

            for i in a:
                if i%10==5 :
                    if i!=a[0]:
                        ans=False
                        break
                else:
                    if i-5!=a[0]:
                        ans=False
                        break
        if ans:
            print("YES")
        else:
            print("NO")

    else:
        p=None
        s=set()
        for i in a:
            if i%10==5 or i%10==0:
                ans=False
                break
            
            while i%10!=2:
                i=i+ i%10
            s.add(i%20)

        if len(s)>1:
            ans=False
            

        
        if ans:
            print("YES")
        else:
            print("NO")



        

