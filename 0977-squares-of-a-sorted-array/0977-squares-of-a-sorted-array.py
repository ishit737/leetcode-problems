class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            if nums[right]**2 >= nums[left]**2:
                res[pos] = nums[right]**2
                right = right - 1
            else:
                res[pos] = nums[left]**2
                left = left + 1
            
            pos = pos - 1 

        return res  
            