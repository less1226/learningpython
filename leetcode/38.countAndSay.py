class Solution:
    def countAndSay(self, n: int) -> str:
        count = "1"
        result = ""
        
        for i in range(1,n):
            cur = count[0]
            curcount = 0
            for j in count:
                if cur == j:
                    curcount += 1
                else:
                    result = result + str(curcount) + cur
                    cur = j
                    curcount = 1
                count = result
                
            result = ""   
            count = count + str(curcount) + cur
        
        return count
