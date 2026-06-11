class SegmentTree:
    def __init__(self,n):
        self.x=[0]*(4*n)
    
    def build(self,arr,ind,left,right,orr):
        if left==right:
            self.x[ind]=arr[left]
        else:
            mid=(left+right-1)//2
            self.build(arr,2*ind+1,left,mid,not orr)
            self.build(arr,2*ind+2,mid+1,right,not orr)
            if orr:
                self.x[ind]=self.x[2*ind+1] | self.x[2*ind+2]
            else:    
                self.x[ind]=self.x[2*ind+1] ^ self.x[2*ind+2]
    def update(self,i,val,ind,l,r,orr):
        if l==r:
            self.x[ind]=val
        else:
            mid=(l+r-1)//2
            if i<=mid:
                self.update(i,val,2*ind+1,l,mid, not orr)
                if orr:
                    self.x[ind]=self.x[2*ind+1] | self.x[2*ind+2]
                else:    
                    self.x[ind]=self.x[2*ind+1] ^ self.x[2*ind+2]
            else:
                self.update(i,val,2*ind+2,mid+1,r,not orr)
                if orr:
                    self.x[ind]=self.x[2*ind+1] | self.x[2*ind+2]
                else:    
                    self.x[ind]=self.x[2*ind+1] ^ self.x[2*ind+2]
            

n,m= map(int,input().split())
a=list(map(int,input().split()))
an=len(a)
s=SegmentTree(an)
if n%2!=0:
    s.build(a,0,0,an-1,1)
    for i in range(m):
        i,val= map(int,input().split())
        i-=1
        s.update(i,val,0,0,an-1,1)
        print(s.x[0])
else:
    s.build(a,0,0,an-1,0)
    print(s.x)
    for i in range(m):
        i,val= map(int,input().split())
        i-=1
        s.update(i,val,0,0,an-1,0)
        print(s.x[0])



        