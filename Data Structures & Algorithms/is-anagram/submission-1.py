class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s = defaultdict(int)
        letters_t = defaultdict(int)

        for l in s:
            letters_s[l] += 1
        
        for l in t:
            letters_t[l] += 1

        if letters_s != letters_t:
            return False
            
        return True