#lc-79
#Word Search

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        columns=len(board[0])


        def dfs(row, column, i):
            #base case

            #if word exists in the grid, return true
            if i == len(word):
                return True

            #index out of bounds
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return False

            #current cell is already used, false
            if board[row][column] == "#":
                return False

            #current cell is not matched, false
            if board[row][column] != word[i]:
                return False

                       
            #mark the current cell is already used
            temp=board[row][column]
            board[row][column]= "#"

            found =(
            dfs(row-1, column, i+1) or #up 
            dfs(row+1, column, i+1) or #down
            dfs(row, column-1, i+1) or #left
            dfs(row, column+1, i+1)    #right
            )

            #backtracking, rest the current cell for other path to use
            board[row][column]=temp

            return found

        #iterate through every cell on the grid to treat it as a potential starting point
        for row in range(rows):
            for column in range(columns):
                #if dfs() starting at this cell successfully fins the word, retrun True
                if board[row][column] == word[0] and dfs(row, column, 0):
                    return True

        return False


    



