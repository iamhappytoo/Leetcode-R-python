# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getpath(node):
            if node is None:
                return 0
            childnum=0
            if node.left is not None:
                childnum+=1
            if node.right is not None:
                childnum+=1
            return(getlevel(node.left,0)+getlevel(node.right,0)+childnum)
        
        def getlevel(node,level):
            if node is None:
                return level
            else:
                childnum=0
                if node.left is not None or node.right is not None:
                    childnum=1
                level=max(getlevel(node.right,level),
                          getlevel(node.left,level))+childnum
                return level
        
        if root is None:
            return 0
        queue=[]
        maxpath=0
        queue.append(root)
        while queue:
            node=queue.pop(0)
            maxpath=max(maxpath,getpath(node))
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return maxpath

        
'''
Another solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  diameter = 0
  def longest(root):
    nonlocal diameter
    if root is None:
      return 0
    gleft=longest(root.left)
    gright=longest(root.right)
    diameter=max(diameter,gleft+gright)
    return(1+max(gleft, gright))
  longest(root)
  return diameter
