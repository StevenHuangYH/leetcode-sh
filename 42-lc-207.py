#lc 206
#course schedule

from typing import List
from collections import deque

#Topological Sorting
#in-degree table
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjcency list
        graph=[ [] for _ in range(numCourses)]

        #indegree table
        indegree=[0]*numCourses

        #Iterate over the edge list
        for after, pre in prerequisites:
            graph[pre].append(after)
            indegree[after]+=1

        #initialize the queue
        queue=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)


        while queue: #while queue has value
            cur_class = queue.popleft()
            for after in graph[cur_class]:
                indegree[after]-=1
                if indegree[after]==0:
                    queue.append(after)

        for item in indegree:
            if item != 0:
                return False

        return True
            
        





        