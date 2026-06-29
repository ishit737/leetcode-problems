class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
     
        b=[]
        for i in range(n):
            b.append(nums[i])  
            a=i+(len(nums)//2) 
            b.append(nums[a])
        return b    