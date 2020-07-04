class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        return self.sol(s, set(wordDict), set())
        
            

    def sol(self, s, words, fails):

        if s in words:
            
            return True
        
        else:
            i = 0
            while i < len(s) + 1:
                if s[0 : i] in words:
                    
                    if s[i:] in fails:
                        i += 1
                    elif not self.sol(s[i:], words, fails):
                        fails.add(s[i:])
                        i += 1
                    else:
                        return True
                
                i += 1
            
            return False
