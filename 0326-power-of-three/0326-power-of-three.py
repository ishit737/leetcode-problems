class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        elif 3**19%n==0:
            return True 
        else:
            return False          
        