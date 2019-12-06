class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = -1
            else:
                dic[s[i]] = i

        li = [x for i, x in dic.items() if x != -1]
        li.sort()
        return li[0] if len(li) > 0 else -1
