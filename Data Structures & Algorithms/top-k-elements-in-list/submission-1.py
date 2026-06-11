from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            
        heap = [] # (val, key)
        for key, val in freq.items(): # O(n)
            heapq.heappush(heap, (val, key))
        
        return [x[1] for x in heapq.nlargest(k, heap)]