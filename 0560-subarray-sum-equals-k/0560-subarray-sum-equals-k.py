class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        d = {0: 1}
        counter = 0
        
        for num in nums:
            total += num
            if (total - k) in d:
                counter += d[total - k]
            if total in d:
                d[total] += 1
            else:
                d[total] = 1
        return counter
