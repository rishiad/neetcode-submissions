class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s = defaultdict(int)
        letters_t = defaultdict(int)

        for l in range(len(s)):
            letters_s[s[l]] += 1
            letters_t[t[l]] += 1

        if letters_s != letters_t:
            return False

        return True