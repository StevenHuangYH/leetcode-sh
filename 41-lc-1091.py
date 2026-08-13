#lc1091
#shorest path in binary matrix

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0:
            return -1

        rows=len(grid)
        column=len(grid[0])
        queue=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        #initialize the queue
        queue.append((0,0))

        while queue:
            size=len(queue)
            for _ in range(size):


        