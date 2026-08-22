#lc-77
#Combinations


#backtracking algorithm
#N-ary Tree
#pick or don't pick / 0-1 decision tree


from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #like when n=4, nums=[1,2,3,4]
        nums=[i for i in range(1, n+1)]
        result=[]

        def backtrack(path, start_index):
            if len(path)==k:
                result.append(path[:]) #deepcopy
                return


            for i in range (start_index, len(nums)): # in charge horizontal of the n-ary tree
                path.append(nums[i]) #make selection
                                     #recursion in charge the vertical part
                backtrack(path, i+1) #recursive, pass through next index and path 
                #path is a list

                path.pop()#cancel the selection / backtracking


        backtrack([], 0) #empty list for path. as the resusion goes deeper, numbers will be added to it
                         # starting index from 0
        return result 
        


class Solution2:
    def combine(self,n:int , k:int)-> List[List[int]]:
                #like when n=4, nums=[1,2,3,4]
        nums=[i for i in range(1, n+1)]
        result=[]
        path=[]

        def backtrack(start_index):
            if len(path)==k:
                result.append(path[:]) #deepcopy
                return


            for i in range (start_index, len(nums)): # in charge horizontal of the n-ary tree
                path.append(nums[i]) #make selection
                                     #recursion in charge the vertical part
                backtrack( i+1) #recursive, pass through next index and path 
                #path is a list

                path.pop()#cancel the selection / backtracking


        backtrack( 0) #empty list for path. as the resusion goes deeper, numbers will be added to it
                         # starting index from 0
        return result 




#0-1 decision tree
class Solution3:
    def combine(self, n:int, k:int) -> List[List[int]]:
        result=[]
        path=[]

        def backtrack(cur_num): #cur_num -> pointer for tracking num
            if len(path)==k:
                result.append(path[:]) #deepcopy
                return


            if cur_num > n: #edge case for the pointer
                return

            #pick
            path.append(cur_num)
            backtrack(cur_num+1)

            #backtrack
            path.pop()
            
            #not pick
            backtrack(cur_num+1)

        backtrack(1)
        return result

    