from collections import defaultdict, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [] # (val, key)
        for key, val in freq.items(): # O(n)
            heapq.heappush(heap, (val, key))
        
        return [x[1] for x in heapq.nlargest(k, heap)]