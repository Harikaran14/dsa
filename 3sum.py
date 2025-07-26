nums = [-2,-2,-1, -1, 0, 0, 1, 1, 2, 2]

op=[]
nums.sort()
for i in range(len(nums)):
    if i>0 and nums[i] == nums[i-1]:
        continue
    l=i+1
    r=len(nums)-1
    while l<r:
        x=nums[l]+nums[r]+nums[i]
        if x>0  :
            r-=1
        elif x<0 :
            l+=1
        elif x==0 :
            op.append([nums[i],nums[l],nums[r]])
            l+=1
            r-=1
                    
            while l<r and    nums[l]==nums[l-1]:
                l+=1
print(op)