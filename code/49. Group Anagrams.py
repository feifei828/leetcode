class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for obj in strs:
            key = ''.join(sorted(obj))
            if not d.get(key, None):
                d[key] = [obj]
            else:
                d[key].append(obj)
        return [v for k, v in d.items()]