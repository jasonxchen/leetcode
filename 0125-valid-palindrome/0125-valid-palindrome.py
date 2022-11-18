class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_s = ""
        for letter in s:
            code = ord(letter)
            if code >= 48 and code <= 57 or code >= 97 and code <= 122:
                valid_s += letter
        return valid_s == valid_s[::-1]
