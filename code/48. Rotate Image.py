class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        l = [None for i in range(n ** 2)]
        for role_index, role in enumerate(matrix):
            for col_index, col in enumerate(role):
                l[col_index * n + (n - 1 - role_index)] = col

        for role in matrix:
            for i in range(n):
                role[i] = l.pop(0)
