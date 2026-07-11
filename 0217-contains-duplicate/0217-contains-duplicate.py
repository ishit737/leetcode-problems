class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

   
        return len(nums) != len(set(nums))

    ##brute force,has time complexity O(N^2).other method can be using set(nums) to make it faster
    for i in nums:
        if nums.count(i)>1:
            return True
     return False       

     
