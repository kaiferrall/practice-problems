'''
  @topics: memoization, dynamic programming, arrays
'''
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.find_paths(m, n, {})
    
    
    def find_paths(self, m, n, mem):
        r1, r2 = None, None
        
        if m == 1 or n == 1:
            return 1
        
        if (m, n - 1) in mem:
            r1 = mem[(m, n - 1)]
        
        if (m - 1, n) in mem:
            r2 = mem[(m - 1, n)]
        

        if r1 and r2:
            res = r1 + r2
        elif r1 and not r2:
            res = self.find_paths(m - 1, n, mem) + r1
        elif r2 and not r1:
            res = self.find_paths(m, n - 1, mem) + r2
        else:
            res = self.find_paths(m - 1, n, mem) + self.find_paths(m, n - 1, mem)

        mem[(m, n)] = res
        return res
        
        
        
        
