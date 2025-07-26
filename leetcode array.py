class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        n=len(nums)
        a=0
        while l<n:
            if l>0 and nums[l]==nums[l-1]:    
                nums.append(nums.pop(l))
                a+=1
            elif l<n-1 and  nums[l]==nums[l+1]:
                l+=2
            else:
                l+=1

        nums=nums[:n-a+1]  
        print(nums)      
        return len(nums)      

x=Solution()
print(x.removeDuplicates([1]))