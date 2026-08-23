#lc 130
#surrounded regions
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        columns=len(board[0])

        def dfs(row,column): #replace O as #
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return

            # #if current cell is X, do nothing:
            # if board[row][column]=="X":
            #     return

            # if board[row][column]=="#": 不要走回头路
            #     return   

            if board[row][column]!="O":
                return       

            board[row][column]="#"

            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)

        #Boundary Traversal
        for row in range(rows):
            if board[row][0]=="O":
                dfs(row,0)
            if board[row][columns-1]=="O":
                dfs(row,columns-1)

        for column in range(columns):
            if board[0][column]=="O":
                dfs(0,column)
            if board[rows-1][column]=="O":
                dfs(rows-1,column)

        #travel the entire gird, replace # as O, replace O as X
        for row in range(rows):
            for column in range(columns):
                if board[row][column]=="#":
                    board[row][column]="O"
                elif board[row][column]=="O": #reminder: use elif
                    board[row][column]="X"


                
            
                






