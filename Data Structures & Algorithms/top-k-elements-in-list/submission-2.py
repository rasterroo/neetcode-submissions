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
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

