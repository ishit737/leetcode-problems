class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = set(nums)
        
        a = max(c)
        
        c.remove(a)
        if not c:
            return a
            
        b = max(c)
        
        c.remove(b)
        if not c:
            return a
            
        return max(c)
