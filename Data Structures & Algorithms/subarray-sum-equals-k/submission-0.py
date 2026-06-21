from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # accumulate currSum, create hashmap of prefix sum counts
        # if currsum - k in prefixsums, then there exists subarrays where removing prefixSum
        # from currSum will give a subarray equal to k
        curSum = result = 0
        hmap = defaultdict(int)
        hmap[0] = 1

        for num in nums:
            curSum += num
            target = curSum - k
            result += hmap[target]
            hmap[curSum] += 1

        return result