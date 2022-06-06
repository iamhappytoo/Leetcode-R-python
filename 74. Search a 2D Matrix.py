class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        n = len(matrix)
        if len(matrix[0]) == 0:
            return False
        
        m = len(matrix[0])
        start = 0
        end = n * m - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            row = mid // m 
            col = mid % m 
            if matrix[row][col] < target:
                start = mid
            else:
                end = mid
                
        if matrix[start // m][start % m] == target:
            return True
        if matrix[end // m][end % m] == target:
            return True
        return False
##TC=O(log(mn)), SC=O(1)
