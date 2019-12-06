class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        returnstr = ""
        conti = True
        con = 0
        compare = ""
        
        while conti:
            for i in strs:
                if i == "":
                    compare = ""
                    conti = False
                    break
                if con < len(i):
                    if compare == "":
                        compare = i[con]
                    elif i[con] != compare:
                        compare = ""
                        conti = False
                        break
                else:
                    compare = ""
                    conti = False
                    break
                
            
            if compare != "":
                returnstr = returnstr + compare
                compare= ""
                con += 1
            else:
                break
        return returnstr
