# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = []
        queue.append((root, 0))
        while queue:
            node, column = queue.pop(0)
            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left,column-1)) ##has null so can do.
                queue.append((node.right,column+1))
        
        return [columnTable[x] for x in sorted(columnTable.keys())]
                
