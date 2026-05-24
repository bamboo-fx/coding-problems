class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        # build s1 map
        s1_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)

        # build s2 map
        s2_map = {}
        for r in range(len(s2)):
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0)
            # if window gets too big increment left pointer
            if r - l + 1 > len(s1):
                if s2_map[s2[l]] == 1:
                    del s2_map[s2[l]]
                else:
                    s2_map[s2[l]] -= 1
                l += 1
            if s2_map == s1_map:
                return True

        return False
            