from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [2,-1,1,2], k=2
        # store hashmap of prefix sum counters
        output = 0
        currSum = 0
        pSums = defaultdict(int)
        pSums[0] = 1

        for num in nums:
            currSum += num
            diff = currSum - k
            output += pSums[diff] 
            pSums[currSum] += 1

        return output

