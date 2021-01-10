# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        result = [first]
        for x in encoded:
            result.append(x^result[-1])
        return result
