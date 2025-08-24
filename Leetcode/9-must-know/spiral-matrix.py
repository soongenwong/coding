class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = '.'

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == '.':
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        
        return res

        # initial plan
        # use dfs to find the values. 
        # when it reaches an edge, change direction. 


        # final solution
        # find total numer of rows and columns
        # find total number of rows and columns
        # dx and dy are for directions. 
        # add current element to the result, mark as visited. 
        # rotate. (1,0) is move right, (0, 1) is move down. 
        # add current direction to position. 
        # matrix[row][col] = matrix[y][x]