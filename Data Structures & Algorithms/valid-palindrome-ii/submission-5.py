class Solution:
    def validPalindrome(self, s: str) -> bool:
        j = 0
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i - 1]:
                j = i
                break
            if i == len(s)//2 - 1: 
                return True
        
        s2 = s[0:len(s) - 1 - j] + s[len(s) - j:len(s)]
        s3 = s[0:j] + s[j+1:len(s)]

        s2_errors = 0
        s3_errors = 0


        for k in range(j, len(s2)//2):
            if (s2[k] != s2[len(s2) - k - 1]):
                s2_errors += 1
            if (s3[k] != s3[len(s3) - k - 1]):
                s3_errors += 1
            if s2_errors >= 1 and s3_errors >= 1:
                return False
        return True
