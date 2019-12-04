class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_min = -2**31
        int_max = 2**31-1
        digit = 0
        first = ""
        lis = list(str)
        for i in lis:
            if first == "":
                if i == " ": 
                    continue
                    
                if i.isdigit():
                    digit = int(i)
                    first = "+"
                elif i =="-" or i == "+":
                    first = i
                else:
                    return digit
            else:
                if i.isdigit():
                    digit = digit*10 + int(i)
                    if first=="-" and -digit < int_min:
                        return int_min
                    elif first=="+" and digit > int_max:
                        return int_max
                else:
                    break
                    
        return digit if first=="+" else -digit
