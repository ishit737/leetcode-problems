class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low = 0
        high = len(nums) - 1
        x = -1
        y = -1

        # First occurrence
        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == target:
                x = mid
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        if x>=0: #here i learnt that that Since x is the first occurrence,every index before it is sure to be lesser than target,hence a teeny tiny optimization of using the previous info,so the next search goes from x to n-1 instead of starting from 0.
            low =x
        else: 
            return[-1,-1]
        high = len(nums) - 1

        
        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == target:
                y = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return [x, y]