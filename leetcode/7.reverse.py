class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strx = str(x)
        strnew = ""
        for i in strx[::-1]:
            if i == strx[0] and i == '-':
                strnew = i + strnew
            else:
                strnew = strnew + i

        returnValue = int(strnew)

        if returnValue > 2**31 - 1 or returnValue < -2**31:
            return 0

        return returnValue