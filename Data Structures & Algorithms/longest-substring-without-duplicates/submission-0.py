class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                longest = max(longest, i-left+1)
            else:
                while left < i and s[i] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[i])
                    
        return longest