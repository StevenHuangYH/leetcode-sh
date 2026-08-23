#lc-105

#construct binary tree from preorder and inorder traversal
from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



#pre-order root-left-righ
#inorder: left-root-right

#posterorder: left-right-root


#divide and conquer
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val=preorder[0]
        root=TreeNode(val=root_val)

        root_index=inorder.index(root_val) #O(n)



        #left subtree
        root.left=self.buildTree(preorder[1 : 1+root_index],inorder[:root_index])


        #right subtree
        root.right=self.buildTree(preorder[1 + root_index :],inorder[root_index + 1 :])

        return root



class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val:idx for idx,val in enumerate(inorder)} #hashmap for inorder

        def solver(pre_left, pre_right, in_left, in_right)->Optional[TreeNode]:
            if pre_left>pre_right:
                return None

            root_val=preorder[pre_left]
            root=TreeNode(val=root_val)
            root_idx=inorder_map[root_val] 

            left_size=root_idx-in_left

            root.left= solver(pre_left+1, pre_left+left_size, in_left, root_idx-1)
            root.right= solver(pre_left+left_size+1, pre_right, root_idx+1,in_right)

            return root

        return solver(0, len(preorder)-1, 0, len(inorder)-1)







            

            

            











