class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False   
                end = stack.pop()
                if mapping[c]!=end:
                    return False
        return not stack