# -*- coding:utf-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = sorted(nums)
        res = []
        for i in range(len(l) - 2):
            if i > 0 and l[i] == l[i-1]:
                continue
            j = i + 1
            k = len(l) - 1
            while j < k:
                s = l[i] + l[j] + l[k]
                if s < 0:
                    j += 1
                    while j<k and l[j] == l[j-1]:
                        j += 1
                elif s > 0:
                    k -= 1
                    while j < k and l[k] == l[k+1]:
                        k -= 1
                else:
                    res.append([l[i], l[j], l[k]])
                    j += 1
                    k -= 1
                    while j < k and l[j] == l[j-1]:
                        j += 1
                    while j < k and l[k] == l[k+1]:
                        k -= 1
        return res
