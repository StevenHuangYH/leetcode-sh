from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums


        

    def sumRange(self, left: int, right: int) -> int: #general way
        my_sum = 0
        for i in range(left, right+1):
            my_sum +=self.nums[i]
        return my_sum
            


if __name__ == '__main__':
    a=NumArray([0,1,2,3,4,5,6])
    a.sumRange(0,2)


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)