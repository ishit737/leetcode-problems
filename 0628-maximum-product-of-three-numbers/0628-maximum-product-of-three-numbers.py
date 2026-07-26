class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
     
       """

        if len(nums) < 5:
            nums.sort()
            return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        d=min(nums)
        nums.remove(d)
        e=min(nums)
        nums.remove(e)
      
     
        a=max(nums)
        nums.remove(a)
        b=max(nums)
        nums.remove(b)
        c=max(nums)
      
      
    
        if (a*b*c)>(a*d*e):
            return a*b*c
        else:
            return a*d*e    
           
        
        