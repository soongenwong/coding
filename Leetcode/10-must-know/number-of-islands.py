class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
    

        
       
       # initial plan
       # use matrix to store values
       # loop through the values from left to right, and then continue to next row
       # if there is a "1" on the samer vertical or horizontal grid, add it to the same island.

       # final solution
       # DFS: simpler to implement than BFS, code is more concise. DFS has cleaner code. 
       # base check
       # stop recursion if the cell is out of grid. 
       # mark the cell as visited as zero. 
       # check all 4 adjacent directions. 
       # i represents the row index (vertical position)
       # j represents the column index (horizontal position)
       #len(grid) means vertical and len(grid[0]) means horizontal

