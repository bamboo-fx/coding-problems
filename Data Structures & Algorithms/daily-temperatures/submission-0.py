class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        # brute force it with two pointers
        
        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1
            if j == len(temperatures):
                result.append(0)
                continue
        
            result.append(j-i)
            
        return result