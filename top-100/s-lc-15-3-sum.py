from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        #the order of triple is not matter
        # i< j < k
        #the result cannot includ repeated triples


        result=[]
        n = len(nums)

        for i in range(0, n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue

            #optimization 1
            if x + nums[i+1] + nums[i+2] > 0:
                break

            #optimization 2
            if x + nums[-2] + nums[-1] < 0:
                continue


            j = i + 1
            k = n - 1
            while j < k:
                s = x+ nums[j] + nums[k]
                if s > 0:
                    k-=1
                elif s < 0:
                    j += 1
                else:
                    result.append([x,nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k-=1
        return result


