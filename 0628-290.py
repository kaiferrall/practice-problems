'''
  @difficulty: easy
  @topics: dictionaries
'''

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        words = str.split(' ')
        chars = list(pattern)
        d = {}
        
        if len(words) != len(chars):
            return False
        
        for c, w in zip(chars, words):
           
            if c in d and w not in d.values():
                return False
            elif c not in d and w in d.values():
                return False
            elif c in d and d[c] != w:
                return False
            else:
                d[c] = w
            
        return True