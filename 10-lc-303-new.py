from typing import List
class NumArray: #new

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) + 1) #第i个element的位置储存列表前i个元素的和
        for i in range((len(nums))):
            self.preSum[i+1] = self.preSum[i] + nums[i]



    def sumRange(self, left: int, right: int) -> int: #new
        return self.preSum[right+1] - self.preSum[left]
        

      
            


if __name__ == '__main__':
    a=NumArray([0,1,2,3,4,5,6])
    a.sumRange(0,2)


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)