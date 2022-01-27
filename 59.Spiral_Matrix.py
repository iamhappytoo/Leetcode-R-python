import numpy as np
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = np.zeros((n,n), dtype = np.int32)
        mat[0][:]=[int(x) for x in range(1,n+1)]
        V = [1,0,-1,0]
        H = [0,-1,0,1]
        flag = 0
        cur = n+1
        r = 0
        c = n-1
        for i in range(n-1, 0, -1):
            for j in range(1,i+1):
                c = c + H[flag]
                r = r + V[flag]
                mat[r][c] = int(cur)
                cur += 1
            flag += 1
            flag = flag % 4
            for j in range(1,i+1):
                c = c + H[flag]
                r = r + V[flag]
                mat[r][c] = int(cur)
                cur += 1
            flag += 1
            flag = flag % 4
        
        return mat
            
                 
                 
            
            
            
        
