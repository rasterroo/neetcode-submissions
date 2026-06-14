from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        brute force: for each str, sort it. then that will be key. 
        keep dict for each sorted key, then append to list.
        return list of all dict values (lists)
        n^2 log n 

        better solution: instead of sorting, just map the counts of 
        strs as [0]*26, increment ordinal values . use that as a key 
        then use that tuple as key in dict
        '''
        hmap = defaultdict(list)

        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c) - ord('a')] += 1

            hmap[tuple(counts)].append(s)

        return [l for l in hmap.values()]
            
