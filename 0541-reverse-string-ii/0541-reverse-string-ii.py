class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
   
        char = list(s)
        for i in range(0, len(char), 2 * k):
            char[i : i + k] = reversed(char[i : i + k])
        return "".join(char)
