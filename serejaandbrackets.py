import sys
input=sys.stdin.readline

class Snode:
    def __init__(self):
        self.open=0
        self.close=0
        self.complete=0


class SegmentTree:
    def __init__(self,n):
        self.x=[Snode() for i in range(*(4*n))]
    
    def build(self,arr,ind,left,right):
        if left==right:
            if arr[left]=="(":
                self.x[ind].open+=1
            else:
                self.x[ind].close+=1
        else:
            mid=(left+right)//2
            self.build(arr,2*ind+1,left,mid)
            self.build(arr,2*ind+2,mid+1,right)
            l=self.x[2*ind+1]
            r=self.x[2*ind+2]
            v=min(l.open,r.close)
            self.x[ind].complete= l.complete+r.complete + v
            self.x[ind].open= l.open +r.open - v
            self.x[ind].close=l.close+r.close-v
    
            
    def query(self,ind,left,right,l,r):
        if l<=left<=right<=r:
            return self.x[ind]
        elif l>right or r<left:
            return Snode()
        else:
            root=Snode()
            mid=(left+right)//2
            ll=self.query(2*ind+1,left,mid,l,r)
            rr=self.query(2*ind+2,mid+1,right,l,r)
            v=min(ll.open,rr.close)
            root.complete= ll.complete+rr.complete + v
            root.open= ll.open +rr.open - v
            root.close=ll.close+rr.close-v
            return root
    


inp=input().strip()
n=int(input())
x=len(inp)       
s=SegmentTree(x)

v=s.build(inp,0,0,x-1)
ans=[]
for i in range(n):
    l,r= map(int,input().split())
    l-=1
    r-=1
    ans.append(str(s.query(0,0,x-1,l,r).complete*2))
sys.stdout.write("\n".join(ans))