class Solution(object):
    def shuffle(self, nums, n):
        b = []

        for i in range(n):
            b.append(nums[i])
            b.append(nums[i + n])

        return b  