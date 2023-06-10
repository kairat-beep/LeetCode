from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        trusted = defaultdict(int)
        for i, j in trust:
            trusts[i] = 1
            trusted[j] += 1
        for i in range(1, n + 1):
            if 0 == trusts[i] and trusted[i] == n-1:
                return i 
        return -1
