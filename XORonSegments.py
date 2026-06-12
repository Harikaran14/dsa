import sys
input=sys.stdin.readline
class SegmentTree:
    def __init__(self,n):
        self.x=[[0]*21 for i in range(4*n+1)]
        self.lazy=[0]*(4*n+1)
        self.n=n
    
    def build(self,arr,ind,left,right):
        if left==right:
            for i in range(20):
                self.x[ind][i]=1 if arr[left]&1<<i else 0

        else:
            mid=(left+right)//2
            self.build(arr,2*ind+1,left,mid)
            self.build(arr,2*ind+2,mid+1,right)
            for i in range(21):
                self.x[ind][i]=self.x[2*ind+1][i]+self.x[2*ind+2][i]
    
    def push(self,ind,left,right):
        if self.lazy[ind]==0:
            return
        x=self.lazy[ind]
        for i in range(21):
            if x&(1<<i):
                self.x[ind][i]=(right-left+1)-self.x[ind][i]
        if left!=right:
            self.lazy[2*ind+1]^=x
            self.lazy[2*ind+2]^=x
        self.lazy[ind]=0

    def update(self,left,right,val,ind,l,r):

        self.push(ind,left,right)
        if l<=left<=right<=r:
            self.lazy[ind]^=val
            self.push(ind,left,right)


        elif l>right or r<left:
            return 
        else:
            mid=(left+right)//2
            self.update(left,mid,val,2*ind+1,l,r)
            self.update(mid+1,right,val,2*ind+2,l,r)
            for i in range(21):
                self.x[ind][i]=self.x[2*ind+1][i]+self.x[2*ind+2][i]
    
    def query(self,ind,left,right,l,r):
        self.push(ind,left,right)
        if l<=left<=right<=r:
            ans=0
            for i in range(21):
                ans+=self.x[ind][i]*(1<<i)
            return ans
        elif l>right or r<left:
            return 0
        else:
            mid=(left+right)//2
            ll=self.query(2*ind+1,left,mid,l,r)
            rr=self.query(2*ind+2,mid+1,right,l,r)
            return ll+rr
    

      
n=int(input())
a=list(map(int,input().split()))
m=int(input())
an=len(a)
s=SegmentTree(an)
out=[]
s.build(a,0,0,an-1)
for i in range(m):
    e= list(map(int,input().split()))
    if e[0]==1:
        value=s.query(0,0,an-1,e[1]-1,e[2]-1)
        out.append(value)
    else:
        s.update(0,an-1,e[3],0,e[1]-1,e[2]-1)
    

sys.stdout.write("\n".join(map(str,out)))

