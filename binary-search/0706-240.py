''' 
  @Topics: Binary Search, Divide & Conquer
  @Difficulty: Medium
  @Notes: Could be done cleaner w one function or iteratively.
'''


class Solution:
    def __init__(self):
        self.dropped_cols = self.dropped_rows = set()
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = j = 0
        while i < len(matrix) and j < len(matrix[i]):
            
            res1 = self.search_row(i, matrix, target)
            res2 = self.search_col(j, matrix, target)
            
            if res1 or res2:
                return True
            else:
                i += 1
                j += 1
        
        return False
        
    
    def search_row(self, row, matrix, target):
        if row in self.dropped_rows:
            return False
        
        l = 0
        r = len(matrix[row]) - 1
        
        while l <= r:
            mid = int((r + l) / 2)
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                self.dropped_cols.add(mid)
                r = mid - 1
                
        return False
    
    def search_col(self, col, matrix, target):
        if col in self.dropped_cols:
            return False
        
        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            mid = int((r + l) / 2)
            
            if matrix[mid][col] == target:
                return True
            elif matrix[mid][col] < target:
                l = mid + 1
            else:
                self.dropped_rows.add(mid)
                r = mid - 1
                
        return False
