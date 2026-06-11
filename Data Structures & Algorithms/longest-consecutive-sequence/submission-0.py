class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        seen = set(nums)
        output = 1

        for x in seen:
            if x-1 not in seen:
                curr_length = 1 
                while x + curr_length in seen:
                    curr_length += 1
                output = max(output, curr_length)
                
        return output
