def maxSum(mat):
 
    Sum = 0
    for i in range(0, R // 2):
        for j in range(0, C // 2):
         
            r1, r2 = i, R - i - 1
            c1, c2 = j, C - j - 1
                 
            # We can replace current cell [i, j]
            # with 4 cells without changing/affecting
            # other elements.
            Sum += max(max(mat[r1][c1], mat[r1][c2]),
                       max(mat[r2][c1], mat[r2][c2]))
         
    return Sum
 
# Driver Code
if __name__ == "__main__":
 
    R = C = 4
    mat = [[112, 42, 83, 119],
           [56, 125, 56, 49],
           [15, 78, 101, 43],
           [62, 98, 114, 108]]
 
    print(maxSum(mat))
 
# This code is contributed
# by Rituraj Jain
