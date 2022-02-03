# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        columnTable = defaultdict(list)
        queue = []
        queue.append((root, 0))
        min_column=max_column=0
        while queue:
            node, column = queue.pop(0)
            
            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left,column-1)) ##has null so can do.
                queue.append((node.right,column+1))
        
        return [columnTable[x] for x in range(min_column, max_column+1)]
                