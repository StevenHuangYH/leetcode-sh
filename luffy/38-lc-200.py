#lc-200
#number of islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        counter=0

        def dfs(row, column):
            #offside 
            if row < 0 or row >= rows or column <0 or column >= columns:
                return

            #if is water
            if grid[row][column]=="0":
                return

            #if is land
            grid[row][column]= "0"

            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)


        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=="1":
                    counter+=1
                    dfs(row,column)

        return counter

                



            

        
