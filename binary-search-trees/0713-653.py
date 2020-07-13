'''
  @difficulty: easy
  @topics: binary search trees, and sets (kinda)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        difs = set()
        
        def eval(root):
            if not root:
                return False 
            elif root.val in difs:
                return True
            else:
                difs.add(k - root.val)
                return eval(root.left) or eval(root.right)
            
        return eval(root)
        
        