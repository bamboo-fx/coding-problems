class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # linear scan + two pointers extending out

        # find the closest index/number
        idx = 0
        for i in range(len(arr)):
            if abs(x - arr[i]) < abs(x - arr[idx]):
                idx = i

        final_array = [arr[idx]]

        l, r = idx - 1, idx + 1
        # extend outward l and r until you create array of len(k)
        while len(final_array) < k:
            # logic is: 
            # smallest number comes first
            # didn't do out of bounds check
            if l >= 0 and r < len(arr):
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    final_array.append(arr[l])
                    l -= 1
                elif abs(x - arr[r]) < abs(x - arr[l]):
                    final_array.append(arr[r])
                    r += 1
            elif l >= 0:
                final_array.append(arr[l])
                l -= 1
            
            elif r < len(arr):
                final_array.append(arr[r])
                r += 1
        return sorted(final_array)