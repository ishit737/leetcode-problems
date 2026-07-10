class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
      
        n = 0
        m = 0
        for i in sentences:
            m = len(i.split())
            if m > n:
                n = m
        return n
        