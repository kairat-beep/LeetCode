class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = []
        index = 0
        while index < max(len(word1),len(word2)):
            if index < len(word1):
                newString.append(word1[index])
            if index < len(word2):
                newString.append(word2[index])
            index += 1
        return "".join(newString)
