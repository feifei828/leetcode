class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = sorted(nums)
        closest_val = 999999
        closest = 0
        for i in range(len(l) - 2):
            if i > 0 and l[i] == l[i - 1]:
                continue
            j = i + 1
            k = len(l) - 1
            while j < k:
                s = l[i] + l[j] + l[k]
                if abs(s - target) < closest_val:
                    closest_val = abs(s - target)
                    closest = s
                if s < target:
                    j += 1
                    while j < k and l[j] == l[j - 1]:
                        j += 1
                elif s > target:
                    k -= 1
                    while j < k and l[k] == l[k + 1]:
                        k -= 1
                else:
                    j += 1
                    k -= 1
                    while j < k and l[j] == l[j - 1]:
                        j += 1
                    while j < k and l[k] == l[k + 1]:
                        k -= 1
                    return target
        return closest
