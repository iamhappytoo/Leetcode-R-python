class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = []
        queue.append([root,1])
        while queue:
            temp, depth = queue.pop(0)
            if temp.left:
                queue.append([temp.left, depth + 1])
            if temp.right:
                queue.append([temp.right, depth + 1])
        return depth
##Another way is to do recursion (DFS)
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
