class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic_width = {}
        dic_height = {}
        dic_1 = {}
        dic_2 = {}
        dic_3 = {}
        for i in range(len(board)):
            dic_width.clear()
            dic_height.clear()
            if i == 3 or i == 6:
                dic_1.clear()
                dic_2.clear()
                dic_3.clear()

            for j in range(len(board[i])):
                '''check horizontal line'''
                if board[i][j] != '.':
                    if board[i][j] in dic_width or int(board[i][j]) < 1 or int(
                            board[i][j]) > 9:
                        return False
                    else:
                        dic_width[board[i][j]] = 0
                        if j < 3:
                            if board[i][j] in dic_1:
                                return False
                            else:
                                dic_1[board[i][j]] = 0
                        elif 3 <= j < 6:
                            if board[i][j] in dic_2:
                                return False
                            else:
                                dic_2[board[i][j]] = 0
                        elif 6 <= j < 9:
                            if board[i][j] in dic_3:
                                return False
                            else:
                                dic_3[board[i][j]] = 0
                '''check vertical line'''
                if board[j][i] != '.':
                    if board[j][i] in dic_height or int(
                            board[j][i]) < 1 or int(board[j][i]) > 9:
                        return False
                    else:
                        dic_height[board[j][i]] = 0
        return True
