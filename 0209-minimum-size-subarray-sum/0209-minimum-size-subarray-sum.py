class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        cs=0
        minlen=len(nums)+1
        for i in range(len(nums)):
            cs+=nums[i]
            while cs >= target:
                minlen=min(minlen, i-left+1)

                cs -= nums[left]
                
                left += 1
                
        if minlen==len(nums)+1:
            return 0
        return minlen    





        