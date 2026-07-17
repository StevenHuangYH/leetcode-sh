#lc-56
#Merge Intervals
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

      #need to be sorted first
        # def get_start_num(nums):
        #     return nums[0]
        # intervals.sort(get_start_num)

        #or use lambda [input : return] simplify funtion express
        intervals.sort(key=lambda x:x[0])


        #merge
        res = []
        i=0
        cur = intervals[0]

        while i+1<len(intervals):
            next=intervals[i+1]
            if cur[1]>=next[0]:  #overlapped
                cur[1]=max(cur[1],next[1])
            else: #if not overlapped
                res.append(cur)
                cur=next
            i=i+1
        res.append(cur)
            
        return res



        







