class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A=[]
        B=[]    
            
        for i in range(len(nums)):
            if i==1:
                B.append(nums[1])
            elif i==2:
                A.append(nums[i])
            elif i%2==0:
                B.append(nums[i]) 
            else:
                q=True    
                for x in range(3,int(i**0.5)+1,2):
                    if i%x==0:
                        q=False
                        break
                if q:
                    A.append(nums[i])
                else:
                    B.append(nums[i])

        return abs(sum(A)-sum(B))                       
                


            