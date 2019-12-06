class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
            if s[start].isalnum() == False:
                start += 1
            if s[end].isalnum() == False:
                end -= 1

        return True
