class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        if not nums:
            return [-1, -1]

        while i < j and nums[i] < target:
            i += 1
        while i < j and nums[j] > target:
            j -= 1
        if nums[i] == target and nums[j] == target:
            return [i, j]
        else:
            return [-1, -1]
