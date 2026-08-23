#lc-131

#Palindrome Partitioning

#A palindrome is a string that reads the same forward and backward.
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]

        def is_palindrome(left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def dfs(start_index):
            if start_index>=len(s):
                result.append(path.copy())
                return

            for i in range(start_index, len(s)):
                if is_palindrome(start_index, i):
                    path.append(s[start_index:i+1])
                    dfs(i+1)
                    path.pop()


        dfs(0)
        return result


#pick or not pick solution
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]

        def dfs(starting_index, i):
            if starting_index==len(s):
                result.append(path.copy())
                return
            if i==len(s):
                return

            #need the cur_string and check the next string
            dfs(starting_index,i+1)


            temper_str=s[starting_index:i+1]
            if temper_str==temper_str[::-1]: #string reversed
                path.append(temper_str)
                dfs(i+1,i+1)
                path.pop()


        dfs(0,0)
        return result




            


                
