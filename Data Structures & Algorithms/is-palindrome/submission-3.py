class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
        a = ""
        for i in s:
            if i.lower() in chars:
                a = a + i.lower()
        if a == a[::-1]:
            return True
        else:
            return False


        