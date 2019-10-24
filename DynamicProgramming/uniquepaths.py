class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        def find_paths(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i < 1 or j < 1:
                return 0
            elif i == 1 and j == 1:
                return 1

            elif i == 1:
                path1 = find_paths(i, j-1)
                memo[(i, j-1)] = path1
                return path1
            elif j == 1:
                path2 = find_paths(i-1, j)
                memo[(i-1, j)] = path2
                return path2

            else:
                path1 = find_paths(i-1, j)
                memo[(i-1, j)] = path1
                path2 = find_paths(i, j-1)
                memo[(i, j-1)] = path2

                return path1 + path2



        return find_paths(m,n)
