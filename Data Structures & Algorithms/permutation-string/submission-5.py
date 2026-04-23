class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # basically maintain a window of len(s1) and within it when
        # looping through s2, see if frequency is same
        freq = {}
        for i in range(len(s1)):
            freq[s1[i]] = 1 + freq.get(s1[i], 0)
        r, l = 0, 0
        outer = {}
        while r < len(s2):
            while r < len(s2) and (r - l + 1) <= len(s1):
                outer[s2[r]] = 1 + outer.get(s2[r], 0)
                if (r - l + 1) == len(s1):
                    if outer == freq:
                        return True
                    outer[s2[l]] -= 1
                    if outer[s2[l]] == 0:
                        del outer[s2[l]]
                    l += 1
                r += 1


        return False