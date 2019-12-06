class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = {}
        dic_t = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dic_s[s[i]] = dic_s[s[i]] + 1 if s[i] in dic_s else 1
            dic_t[t[i]] = dic_t[t[i]] + 1 if t[i] in dic_t else 1

        for key, item in dic_t.items():
            if key not in dic_s:
                return False
            elif item != dic_s[key]:
                return False

        return True
