'''
  @difficulty: easy
  @topics: dynamic programming
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        
        return self.helper(0, 1, n, mem) + self.helper(0, 2, n, mem)
    
    
    def helper(self, total, step, n, mem):
        
        if total + step in mem:
            return mem[total + step]
        elif total + step == n:
            return 1
        elif total + step > n:
            return 0
        else:
            res = self.helper(total + step, 2, n, mem)  + self.helper(total + step, 1, n, mem)
            mem[total + step] = res
            
            return res