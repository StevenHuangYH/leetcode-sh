from typing import List


# use for loop
# mat[row][column]
# i -> row  up to buttom index
# j -> left to right index
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [
            [0]*n for _ in range(n)
        ]
        count = 1
        init_index = 0

        while not count >= n**2: #跳出循环条件取反
            for j in range(init_index, n-1-init_index):
                mat[init_index][j] = count
                count += 1
            for i in range(init_index, n-1-init_index):
                mat[i][n-1-init_index] = count
                count += 1
            for j in range(n-1-init_index, init_index, -1):
                mat[n-1-init_index][j] = count
                count += 1
            for i in range(n-1-init_index, init_index, -1):
                mat[i][init_index]= count
                count += 1

            init_index += 1
        
        if n%2==1:
            mat[n//2][n//2]=count
        return mat


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))



    
