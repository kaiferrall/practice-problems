'''
  @difficulty: easy
  @topics: backtracking, permutations
'''
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def sol(s, i):
            res = []
            if i == len(s) - 1:
                if s[i].isalpha():
                    return [s[i], s[i].swapcase()]
                else:
                    return [ s[i] ]
                
            permutations = sol(s, i + 1)
            
            for c in permutations:
                res.append(s[i] + c)
                if s[i].isalpha():
                    res.append(s[i].swapcase() + c)
                    
            return res
        
        return sol(S, 0)
    
    