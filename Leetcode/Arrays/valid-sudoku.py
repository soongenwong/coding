class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[r].add(board[r][c])
                boxes[(r // 3, c //3)].add(board[r][c])
        
        return True
        


        # initial plan
        # save the values in lists
        # use for loops to search for values in the same row, same column and same 3x3 box

        # final solution
        # keep number we found and find duplicate
        # if the spot is empty, continue searching
        # if the number is found in the default dict, return false
        # after you found the number, add it to default dict.