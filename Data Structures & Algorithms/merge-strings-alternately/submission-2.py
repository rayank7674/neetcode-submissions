class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        i, j = 0, 0
        ans = ""
        while True:
            if i < len1:
                ans += word1[i]
                i += 1
            if j < len2:
                ans += word2[j]
                j += 1
            if i >= len1 and j >= len2:
                break
        return ans