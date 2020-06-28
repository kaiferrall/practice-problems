'''
  @difficulty: easy
  @topics: xor
'''
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        xsum = 0
        
        for i in range(n):
            
            xsum ^= start + 2 * i
            
        return xsum