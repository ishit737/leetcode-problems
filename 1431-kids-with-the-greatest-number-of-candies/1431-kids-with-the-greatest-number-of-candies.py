class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        """
        c=max(candies)
        r=[]
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=c:
             r.append(True)
            else:
             r.append(False)

        return r            
    
    