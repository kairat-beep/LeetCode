class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximum= 1
        maxTuple = (0,0)
        for index in range(0,len(s)):
            i = j = index
            #Odd lenght possible
            while i>=0 and j<len(s):
                if s[i] == s[j]:
                    if maximum < j-i+1:
                        maximum = j-i +1
                        maxTuple = (i,j)
                    i = i - 1
                    j = j + 1
                else:
                    break
            i, j = index, index + 1
            #Even length possible
            while i>=0 and j<len(s):
                if s[i] == s[j]:
                    if maximum < j-i+1:
                        maximum = j-i +1
                        maxTuple = (i,j)
                    i = i - 1
                    j = j + 1
                else:
                    break
        (start,end) = maxTuple
        return s[start:end+1]
