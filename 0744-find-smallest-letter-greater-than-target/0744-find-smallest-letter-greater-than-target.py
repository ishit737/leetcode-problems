class Solution(object):
    def nextGreatestLetter(self, letters, target):
        high = len(letters) - 1
        low = 0

        a = letters[0]

        while low <= high:
            mid = low + (high - low) // 2

            if letters[mid] > target:
                a = letters[mid]
                high = mid - 1

            else:
                low = mid + 1

        return a