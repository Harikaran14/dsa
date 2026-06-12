
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
            temp=1<<(self.n.bit_length()-1)
            while temp:
                if ans+temp<=self.n and self.x[ans+temp]<val:
                    
                    val-=self.x[ans+temp]
                    ans+=temp
                temp>>=1
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
temp=1<<(n.bit_length()-1)
while temp:
    if ans+temp<=n and f.x[ans+temp]<val:
        
        val-=f.x[ans+temp]
        ans+=temp
    temp>>=1
if ans!=0:
    ans+=1
print(ans)

