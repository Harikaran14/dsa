
n,e=map(int,input().split())
a=list(map(int,input().split()))
q=list(map(int,input().split()))

class Fenwick:

    def __init__(self,n):
        self.x=[0]*(n+1)
        self.n=n

    def update(self,val):
        if val>0:
            while val<=self.n:
                self.x[val]+=1
                val+=(val&-val)
        
        else:
            val=abs(val)
            #find position and remove it 
            #do binary search
            # x is new position
            
            ans=0
            temp=self.n

            while temp:
                if self.x[temp]<val:
                    ans+=temp
                temp-=temp&-temp
            ans+=1
            val=ans
            while val<=self.n:
                self.x[val]-=1
                val+=val&-val


    def query(self,index):
        ans=0
        while index>0:
            ans+=self.x[index]
            index-=index&-index
        return ans


            
f=Fenwick(n)
for i in a:
    f.update(i)
for i in q:
    f.update(i)
ans=0
l=1
r=n
while l<=r:
    mid=(l+r)//2
    if f.query(mid)>=1:
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)

