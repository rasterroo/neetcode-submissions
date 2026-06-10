from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        for letter, count in c1.items():
            if letter not in c2 or c2[letter]!=count:
                return False
        for letter, count in c2.items():
            if letter not in c1 or c1[letter]!=count:
                return False

        return True