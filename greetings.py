t=int(input())
for _ in range(t):
    x=[]
    n = int(input())
    for i in range(n):
        v=list(map(int,input().split()))
        x.append(v)
    x.sort()
    b=[]
    for i in x:
        b.append(i[1])
    

    def reversePairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
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
                if l[left]>r[right]:
                    ans+=len(l)-left
                    right+=1
                else:
                    left+=1
            left=0
            right=0
            while left<len(l) and right<len(r):
                if l[left]<r[right]:
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
    print(reversePairs(b))
