# Unique path is a unique coding challenge because we have to calculate how many paths that robot will find its destiny. 
# You can check this coding challenge in Leetcode

# There will be a matrix for robot and robot can only move right and down. For instance, there is a matrix 7x3 and calculate the
# paths.

# input => m = 3, n = 2
# output => 3

# Time and space complexity to solve this challenge:
# - Time complexity, I am going to iterate every rows and columns, so it will be O(m * n).
# - Space complexity, same with time complexity where I have to save the calculation in the variable until I get the sum of paths

# Lets code:

class solution():
    def uniquepaths(self, m, n):
        matrix = []
        for i in range(m):
            matrix.append([0]*3)
        for i in range(m):
            matrix[i][0] = 1
        for j in range(n):
            matrix[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[m-1][n-1]
        
solution().uniquepaths(3, 2)
