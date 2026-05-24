class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        max_repeat = 0
        l = 0
        for r in range(len(s)):
            check[s[r]] = 1 + check.get(s[r], 0)
            while (r - l + 1) - max(check.values()) > k:
                check[s[l]] -= 1
                l += 1
            
            max_repeat = max(max_repeat, r - l + 1)
        return max_repeat