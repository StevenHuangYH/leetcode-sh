
#  lc-739-daily temperature

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        stack=[]
        n = len(temperatures)
        answer = [0]*n

        for i in range(n):
            cur_temperature = temperatures[i]

            while True:
                # comparing the current temperature with the past temp
                if stack!=[] and cur_temperature > temperatures[stack[-1]]:
                    pre_index=stack.pop()
                    answer[pre_index]=i-pre_index 
                else:
                    break

            stack.append(i)

        return answer


if __name__ == '__main__':
    s=Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])


                    


        