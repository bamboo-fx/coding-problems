class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        # build s1_map
        s1_map = [0] * 26
        for c in s1:
            s1_map[ord(c) - ord('a')] += 1

        # create window and increment r and compare with smaller
        s2_map = [0] * 26
        for r in range(len(s2)):
            s2_map[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                s2_map[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if s1_map == s2_map:
                return True
        return False