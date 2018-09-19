class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0
        p = 5
        while n/p >= 1:
            count += n//p
            p *= 5
        return count
print(Solution().trailingZeros(105))
