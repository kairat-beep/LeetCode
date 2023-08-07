class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = dict()

        def helper(i, j):
            nonlocal cache, word1, word2
            
            if i < 0:
                return max(0,j+1)

            if j < 0:
                return max(0,i+1)

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = helper(i - 1, j - 1)
            else:
                cache[(i, j)] = min(
                    helper(i - 1, j - 1) + 1,
                    helper(i - 1, j) + 1,
                    helper(i, j - 1) + 1,
                )
            return cache[(i,j)]
        return helper(len(word1) - 1, len(word2) - 1)
