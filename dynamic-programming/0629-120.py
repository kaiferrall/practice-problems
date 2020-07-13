'''
  @difficulty: medium
  @topics: dynamic programming, arrays
'''

class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        mem = [ [ None for _ in r ] for r in triangle]
        i, j = 0, 0
        
        return self.helper(i, j, triangle, mem)
        
    def helper(self, i, j, triangle, mem):
        
        if i == len(triangle) - 1:
            return triangle[i][j]
        
        elif mem[i][j]:
            return mem[i][j]
        
        else:
            
            res1, res2 = self.helper(i + 1, j, triangle, mem), self.helper(i + 1, j + 1, triangle, mem)
            
            mem[i][j] = triangle[i][j] + min(res1, res2)
            
            return mem[i][j]