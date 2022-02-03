# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        run_sum=0
        def dfs(root, low, high):
            nonlocal run_sum
            if root is None:
                return None
            if root.val < low:
                dfs(root.right, low, high)
            elif root.val > high:
                dfs(root.left, low, high)
            else:
                run_sum+=root.val
                dfs(root.right, low, high)
                dfs(root.left, low, high)
        
        dfs(root, low, high)
        return run_sum
    
                
        
        
