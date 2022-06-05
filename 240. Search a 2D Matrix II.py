class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not target:
            return False
        elif len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
       
        nrow = len(matrix); ncol = len(matrix[0])
        x = nrow - 1
        y = 0
        
        while x >= 0 and y < ncol:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                return True
        
        return False
      
TC: O(m+n), SC: O(1)
