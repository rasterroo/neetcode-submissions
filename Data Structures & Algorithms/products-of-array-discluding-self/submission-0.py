class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = suffix[-1] = 1  # default values

        for i in range(1, n):  # build prefix
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):  # build suffix
            suffix[j] = suffix[j+1] * nums[j+1]
        
        return [prefix[i]*suffix[i] for i in range(n)]

        