class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        
        """
        maxIterations = len(s)//(2*k)
        print(maxIterations)
        iterations = 0
        reverse = ""
        while(iterations < maxIterations):
            reverse = reverse + self.revertUnicode(s[iterations * 2 * k : iterations * 2 * k + k]) +s[iterations * 2 * k + k : iterations * 2 * k + 2*k]
            iterations = iterations + 1
        if len(s) >= maxIterations * k:
            reverse = reverse + self.revertUnicode(s[iterations * 2 * k : iterations * 2 * k + k ]) + s[iterations * 2 * k + k :]
        else:
            reverse = reverse + self.revertUnicode(s[iterations * 2 * k : iterations * 2 * k + k ])
        return reverse
    def revertUnicode(self,string):
        return string.decode('utf8')[::-1].encode('utf8')

