class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # increment r continuously
        # increment l until no longer in hashmap

        check = set()
        longest_window = 0
        l = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            longest_window = max(longest_window, r - l + 1)

        return longest_window