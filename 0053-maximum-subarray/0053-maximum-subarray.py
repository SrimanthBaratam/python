class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi,temp=nums[0],nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i],nums[i]+temp)
            maxi=max(maxi,temp)
        return maxi