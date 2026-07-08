class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        for i in address:
           return address.replace(".","[.]")  