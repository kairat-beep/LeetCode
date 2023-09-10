class Solution:
    def reverseVowels(self, s: str) -> str:
        v_pos = []
        vowels = ['a', 'e', 'i', 'o','u']
        vowels = set(vowels + [_.upper() for _ in vowels])
        new_str = list(s)
        i = 0
        j = len(new_str) - 1
        while i < j:
            while(j>-1 and s[j] not in vowels):
                j -= 1
            while(i < len(s) and s[i] not in vowels):
                i += 1
            if i < j:
                temp = new_str[i]
                new_str[i] = new_str[j]
                new_str[j] = temp
            i += 1
            j -= 1
        return "".join(new_str)

