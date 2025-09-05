class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_k = float('-inf')  # potential nums[k] in 132 pattern
        stack = []
        
        # Traverse from right to left to maintain potential nums[j] in stack
        for num in reversed(nums):
            # If current number is less than max_k, we found the pattern
            if num < max_k:
                return True
            else:
                # Pop elements smaller than current num, these are candidates for nums[k]
                while stack and stack[-1] < num:
                    max_k = stack.pop()
            # Push current number as a potential nums[j]
            stack.append(num)
        
        return False

        