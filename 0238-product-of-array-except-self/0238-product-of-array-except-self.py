class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.count(0)>=2:return[0]*len(nums)
        else :
            prod=1
            for i in nums:
                if i:prod*=i
            mul=[1]*len(nums)
            if 0 in nums:
                for i in range(len(nums)):
                    if nums[i]==0:mul[i]=prod
                    else:mul[i]=0
            else:
                for i in range(len(nums)):
                    mul[i]=prod//nums[i]
            return mul