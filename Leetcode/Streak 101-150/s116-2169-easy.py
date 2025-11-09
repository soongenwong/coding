class Solution:
    def countOperations(self, x: int, y: int) -> int:
        return 0 if y==0 else x//y+self.countOperations(y, x%y)
        