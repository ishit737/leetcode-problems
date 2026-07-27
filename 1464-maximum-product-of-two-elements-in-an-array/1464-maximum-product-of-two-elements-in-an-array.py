class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        nums.remove(a)
        b=max(nums)
        return (a-1)*(b-1)

        