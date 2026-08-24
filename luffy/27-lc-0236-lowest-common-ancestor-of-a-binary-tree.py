#lc-236
#the lowest common ancestor of a binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#DFS
#Poster-order: left-right-root

class Solution:
    #retrun the completed information
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode | None':
        #defind return values:
        #whetrher the current node's subtree contains p / whether the current node is the ancestor of p 
        #whether the current node's subtree contains q 
        #and the address of the lowest common ancestor x


        def dfs(node):
            #base case
            if node is None:
                return False, False, None

            left_has_p, left_has_q, left_x = dfs(node.left)
            right_has_p, right_has_q, right_x = dfs(node.right)

            cur_has_p=left_has_p or right_has_p or node == p
            cur_has_q=left_has_q or right_has_q or node == q

            cur_x = None

            if left_x:
                cur_x=left_x
            elif right_x:
                cur_x=right_x
            elif cur_has_p and cur_has_q:
                cur_x=node

            return cur_has_p, cur_has_q, cur_x

        _,_,x=dfs(root)
        return x
        
            





            
            
            

        