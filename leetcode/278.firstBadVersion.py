# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1 if isBadVersion(1) else 0

        middle = n // 2
        start = 1
        end = n
        while start != end:
            if not isBadVersion(middle):
                start = middle + 1
            else:
                end = middle

            offset = (end - start) // 2
            middle = offset + start

        return end