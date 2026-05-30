
x=[]
n = int(input())
for i in range(n):
    v=list(map(int,input().split()))
    x.append([v[1],v[0],i])
x.sort()
b=[]
for i in x:
    b.append([i[1],i[2]])

def reversePairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans=[-1,-1]
    def mergesort(left,right):
        if right-left==0:
            return nums[left:right+1]
        mid=(left+right)//2
        l=mergesort(left,mid)
        r=mergesort(mid+1,right)
        return merge(l,r)
    def merge(l,r):
        nonlocal ans
        y=[]
        left=0
        right=0
        while left<len(l) and right<len(r):
            if l[left][0]>r[right][0]:
                ans=[l[left][1],r[right][1]]
                right+=1
            else:
                left+=1
        left=0
        right=0
        while left<len(l) and right<len(r):
            if l[left][0]<r[right][0]:
                y.append(l[left])
                left+=1
            else:
                y.append(r[right])
                right+=1
        while left<len(l):
            y.append(l[left])
            left+=1
        while right<len(r):
            y.append(r[right])
            right+=1
        
        return y
    n=len(nums)
    x=mergesort(0,n-1)
    return ans
print(*reversePairs(b))