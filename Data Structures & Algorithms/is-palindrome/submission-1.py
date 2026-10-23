class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(ch for ch in s if ch.isalnum())
        text = text.lower()
        for i in range(len(text)//2):
            if text[i] != text[len(text) - i - 1]:
                return False
        return True
