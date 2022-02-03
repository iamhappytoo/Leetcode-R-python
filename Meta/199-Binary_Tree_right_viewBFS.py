# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        rightside=[]
        queue=[]
        queue.append(root)
        while queue:
            levellength=len(queue)
            for i in range(levellength):
                node=queue.pop(0)
                if i==levellength-1:
                    rightside.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return rightside
                    
                