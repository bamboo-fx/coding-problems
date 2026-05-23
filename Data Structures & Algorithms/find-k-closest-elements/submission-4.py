class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search with two pointers

        # binary search to find where x fits

        l, r = 0, len(arr) - 1
        while l < r:
            middle = (l+r) // 2
            if arr[middle] < x:
                l = middle + 1
            else:
                r = middle
            
        # expand out with two pointers until we have an array of length k
        index = l
        l, r = index - 1, index
        res = []
        while (r - l - 1) < k:
            if l >= 0 and r < len(arr):
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < len(arr):
                res.append(arr[r])
                r += 1

        return sorted(res)
        # logic is checking which is smaller then adding
        # add only if possible to increment if either one not increment other

