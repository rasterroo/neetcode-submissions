from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1 
        
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (val, key))

        result = [t[1] for t in heapq.nlargest(k, heap)]
        
        return result

